# Copyright (c) 2025-2026 v4lkyr0 — Buildware-Tools
# See the file 'LICENSE' for copying permission.
# --------------------------------------------------------
# EN: Non-commercial use only. Do not sell, remove credits
#     or redistribute without prior written permission.
# FR: Usage non-commercial uniquement. Ne pas vendre, supprimer
#     les crédits ou redistribuer sans autorisation écrite.

from Plugins.Utils import *
from Plugins.Config import *

try:
    import ast
    import base64
    import builtins
    import marshal
    import random
    import string
    import zlib
except Exception as e:
    MissingModule(e)

Title("Python Obfuscator")

Scroll(GradientBanner(utilities_banner))

protected_names = set(dir(builtins)) | {
    "self", "cls", "__name__", "__main__", "__file__", "__doc__",
    "__init__", "__new__", "__del__", "__repr__", "__str__", "__len__",
    "__iter__", "__next__", "__getitem__", "__setitem__", "__delitem__",
    "__contains__", "__call__", "__enter__", "__exit__", "__eq__", "__ne__",
    "__lt__", "__le__", "__gt__", "__ge__", "__hash__", "__bool__",
    "__add__", "__sub__", "__mul__", "__truediv__", "__floordiv__",
    "__mod__", "__pow__", "__and__", "__or__", "__xor__", "__lshift__",
    "__rshift__", "__neg__", "__pos__", "__abs__", "__invert__",
    "__class__", "__dict__", "__module__", "__qualname__", "__slots__",
    "__all__", "__version__", "__author__", "__annotations__",
    "True", "False", "None",
}

anti_debug_prelude = '''
def _AntiDbg():
    import sys, os, time
    if sys.gettrace() is not None:
        os._exit(0)
    t0 = time.perf_counter()
    for _i in range(1000):
        pass
    if (time.perf_counter() - t0) > 0.5:
        os._exit(0)
    for _v in ("PYTHONBREAKPOINT", "PYTHONINSPECT"):
        if os.environ.get(_v):
            os._exit(0)
_AntiDbg()
del _AntiDbg
'''

def RandomName(length=10):
    return "_Bw_" + "".join(random.choices(string.ascii_letters + string.digits, k=length))

def RandVar():
    return "_bw" + "".join(random.choices(string.ascii_letters + string.digits, k=7))

class IdentifierCollector(ast.NodeVisitor):
    def __init__(self):
        self.defined    = set()
        self.imported   = set()
        self.attributes = set()

    def visit_FunctionDef(self, node):
        if not node.name.startswith("__"):
            self.defined.add(node.name)
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        self.visit_FunctionDef(node)

    def visit_ClassDef(self, node):
        if not node.name.startswith("__"):
            self.defined.add(node.name)
        self.generic_visit(node)

    def visit_Assign(self, node):
        for target in node.targets:
            self.CollectTargets(target)
        self.generic_visit(node)

    def visit_AnnAssign(self, node):
        self.CollectTargets(node.target)
        self.generic_visit(node)

    def visit_AugAssign(self, node):
        self.CollectTargets(node.target)
        self.generic_visit(node)

    def visit_For(self, node):
        self.CollectTargets(node.target)
        self.generic_visit(node)

    def CollectTargets(self, target):
        if isinstance(target, ast.Name):
            self.defined.add(target.id)
        elif isinstance(target, (ast.Tuple, ast.List)):
            for elt in target.elts:
                self.CollectTargets(elt)

    def visit_Import(self, node):
        for alias in node.names:
            name = alias.asname if alias.asname else alias.name.split(".")[0]
            self.imported.add(name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        for alias in node.names:
            name = alias.asname if alias.asname else alias.name
            self.imported.add(name)
        self.generic_visit(node)

    def visit_Attribute(self, node):
        self.attributes.add(node.attr)
        self.generic_visit(node)

class Renamer(ast.NodeTransformer):
    def __init__(self, mapping):
        self.mapping = mapping

    def visit_Name(self, node):
        if node.id in self.mapping:
            node.id = self.mapping[node.id]
        return node

    def visit_FunctionDef(self, node):
        if node.name in self.mapping:
            node.name = self.mapping[node.name]
        for arg in node.args.args + node.args.kwonlyargs:
            if arg.arg in self.mapping:
                arg.arg = self.mapping[arg.arg]
        self.generic_visit(node)
        return node

    def visit_AsyncFunctionDef(self, node):
        return self.visit_FunctionDef(node)

    def visit_ClassDef(self, node):
        if node.name in self.mapping:
            node.name = self.mapping[node.name]
        self.generic_visit(node)
        return node

    def visit_arg(self, node):
        if node.arg in self.mapping:
            node.arg = self.mapping[node.arg]
        return node

def RenameIdentifiers(tree):
    collector  = IdentifierCollector()
    collector.visit(tree)
    renamable  = collector.defined - collector.imported - protected_names
    renamable  = {n for n in renamable if not n.startswith("__")}
    renamable -= collector.attributes
    used_names = set()
    mapping    = {}
    for name in renamable:
        while True:
            new = RandomName()
            if new not in used_names:
                used_names.add(new)
                mapping[name] = new
                break
    tree = Renamer(mapping).visit(tree)
    ast.fix_missing_locations(tree)
    return tree

class LiteralObfuscator(ast.NodeTransformer):
    def visit_Import(self, node):
        return node

    def visit_ImportFrom(self, node):
        return node

    def visit_JoinedStr(self, node):
        return node

    def visit_FormattedValue(self, node):
        return node

    def visit_Expr(self, node):
        if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
            return node
        self.generic_visit(node)
        return node

    def visit_Constant(self, node):
        if isinstance(node.value, str) and len(node.value) > 0:
            return self.EncodeString(node.value)
        if isinstance(node.value, int) and not isinstance(node.value, bool):
            return self.EncodeInt(node.value)
        return node

    def EncodeString(self, s):
        encoded = base64.b64encode(s.encode()).decode()
        expr    = ast.Call(
            func=ast.Attribute(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Call(
                            func=ast.Name(id="__import__", ctx=ast.Load()),
                            args=[ast.Constant(value="base64")],
                            keywords=[],
                        ),
                        attr="b64decode",
                        ctx=ast.Load(),
                    ),
                    args=[ast.Constant(value=encoded)],
                    keywords=[],
                ),
                attr="decode",
                ctx=ast.Load(),
            ),
            args=[],
            keywords=[],
        )
        return ast.copy_location(expr, ast.Constant(value=s))

    def EncodeInt(self, n):
        if abs(n) > 10_000_000:
            return ast.Constant(value=n)
        strategy = random.choice(["xor", "add_sub", "mul_div"])
        if strategy == "xor":
            key  = random.randint(1, 0xFFFF)
            return ast.BinOp(left=ast.Constant(value=n ^ key), op=ast.BitXor(), right=ast.Constant(value=key))
        elif strategy == "add_sub":
            offset = random.randint(1, 10000)
            return ast.BinOp(left=ast.Constant(value=n + offset), op=ast.Sub(), right=ast.Constant(value=offset))
        else:
            if n == 0:
                return ast.BinOp(left=ast.Constant(value=7), op=ast.Sub(), right=ast.Constant(value=7))
            factor = random.randint(2, 7)
            return ast.BinOp(
                left=ast.BinOp(left=ast.Constant(value=n * factor), op=ast.FloorDiv(), right=ast.Constant(value=factor)),
                op=ast.Add(),
                right=ast.Constant(value=0),
            )

def ObfuscateLiterals(tree):
    tree = LiteralObfuscator().visit(tree)
    ast.fix_missing_locations(tree)
    return tree

def BuildJunkStmt():
    kind = random.choice(["assign", "dead_if", "false_cmp"])
    if kind == "assign":
        return ast.Assign(
            targets=[ast.Name(id=RandomName(), ctx=ast.Store())],
            value=ast.Constant(value=random.randint(0, 99999)),
        )
    elif kind == "dead_if":
        name = RandomName()
        return ast.If(
            test=ast.Constant(value=False),
            body=[
                ast.Assign(targets=[ast.Name(id=name, ctx=ast.Store())], value=ast.Constant(value=random.randint(1, 100))),
                ast.AugAssign(target=ast.Name(id=name, ctx=ast.Store()), op=ast.Mult(), value=ast.Constant(value=random.randint(2, 9))),
            ],
            orelse=[],
        )
    else:
        return ast.If(
            test=ast.Compare(
                left=ast.Constant(value=random.randint(1, 100)),
                ops=[ast.Eq()],
                comparators=[ast.Constant(value=random.randint(101, 200))],
            ),
            body=[ast.Pass()],
            orelse=[],
        )

class JunkInjector(ast.NodeTransformer):
    def __init__(self, intensity=0.25):
        self.intensity = intensity

    def Inject(self, body):
        if not body:
            return body
        new_body = []
        for stmt in body:
            if random.random() < self.intensity:
                junk = BuildJunkStmt()
                ast.fix_missing_locations(junk)
                new_body.append(junk)
            new_body.append(stmt)
        return new_body

    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        node.body = self.Inject(node.body)
        return node

    def visit_AsyncFunctionDef(self, node):
        return self.visit_FunctionDef(node)

    def visit_Module(self, node):
        self.generic_visit(node)
        import_end = 0
        for i, stmt in enumerate(node.body):
            if isinstance(stmt, (ast.Import, ast.ImportFrom)):
                import_end = i + 1
        header     = node.body[:import_end]
        body       = node.body[import_end:]
        node.body  = header + self.Inject(body)
        return node

def InjectJunkCode(tree, intensity=0.25):
    tree = JunkInjector(intensity).visit(tree)
    ast.fix_missing_locations(tree)
    return tree

def RemoveDocstrings(tree):
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Module)):
            if (node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Constant) and isinstance(node.body[0].value.value, str)):
                node.body.pop(0)
                if not node.body:
                    node.body.append(ast.Pass())
    ast.fix_missing_locations(tree)
    return tree

def WrapLayer(source, use_marshal=True):
    if use_marshal:
        try:
            code_obj   = compile(source, "<obf>", "exec")
            payload    = marshal.dumps(code_obj)
            compressed = zlib.compress(payload, level=9)
            encoded    = base64.b64encode(compressed).decode("ascii")
            b, z, m    = RandVar(), RandVar(), RandVar()
            return (
                f"{b}=__import__('base64');"
                f"{z}=__import__('zlib');"
                f"{m}=__import__('marshal');"
                f"exec({m}.loads({z}.decompress({b}.b64decode('{encoded}'))))"
            )
        except:
            use_marshal = False

    compressed = zlib.compress(source.encode("utf-8"), level=9)
    encoded    = base64.b64encode(compressed).decode("ascii")
    b, z       = RandVar(), RandVar()
    return (
        f"{b}=__import__('base64');"
        f"{z}=__import__('zlib');"
        f"exec({z}.decompress({b}.b64decode('{encoded}')).decode())"
    )

def Obfuscate(source, level):
    tree = ast.parse(source)
    tree = RemoveDocstrings(tree)
    tree = RenameIdentifiers(tree)

    if level >= 2:
        tree = ObfuscateLiterals(tree)

    if level >= 3:
        tree = InjectJunkCode(tree, intensity=0.3)

    code = ast.unparse(tree)

    layers = {1: 1, 2: 2, 3: 3}
    for i in range(layers[level]):
        code = WrapLayer(code, use_marshal=(i == 0))

    if level >= 2:
        code = anti_debug_prelude + "\n" + code

    return code

try:
    Scroll(f"""
 {PREFIX}01{SUFFIX} Light
 {PREFIX}02{SUFFIX} Medium
 {PREFIX}03{SUFFIX} Strong
""")

    level_choice = input(f"{INPUT} Level {red}->{reset} ").strip().lstrip("0")

    if level_choice not in ["1", "2", "3"]:
        ErrorChoice()

    level = int(level_choice)

    print(f"{INPUT} Select Python File {red}->{reset} ", reset)

    filepath = BrowseFile("Select Python File", [("Python Files", "*.py"), ("All Files", "*.*")])

    if not filepath:
        print(f"{ERROR} No file selected!", reset)
        Continue()
        Reset()

    print(f"{SUCCESS} File:{red} {os.path.basename(filepath)}", reset)

    if not os.path.isfile(filepath):
        print(f"{ERROR} File not found!", reset)
        Continue()
        Reset()

    with open(filepath, "r", encoding="utf-8") as f:
        source = f.read()

    if not source.strip():
        ErrorInput()

    print(f"{LOADING} Obfuscating..", reset)

    try:
        obfuscated = Obfuscate(source, level)
    except SyntaxError:
        print(f"{ERROR} Invalid Python syntax!", reset)
        Continue()
        Reset()

    output_dir  = os.path.join(tool_path, "Programs", "Output", "PythonObfuscator")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, os.path.basename(filepath))

    header = (
        "# Copyright (c) 2025-2026 v4lkyr0 — Buildware-Tools\n"
        "# See the file 'LICENSE' for copying permission.\n"
        "# --------------------------------------------------------\n"
        "# EN: Non-commercial use only. Do not sell, remove credits\n"
        "#     or redistribute without prior written permission.\n"
        "# FR: Usage non-commercial uniquement. Ne pas vendre, supprimer\n"
        "#     les crédits ou redistribuer sans autorisation écrite.\n\n"
    )

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(header + obfuscated)

    print(f"{SUCCESS} Saved:{red} {output_path}", reset)

    if platform_pc == "Windows":
        os.startfile(output_dir)
    else:
        subprocess.Popen(["xdg-open", output_dir])

    Continue()
    Reset()

except Exception as e:
    Error(e)