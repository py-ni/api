
from enum import Enum
from .objects import Dict, Str

from .support import uintptr_t, namespace, utf_string, Self

class Code:

    "To do"


class FrameStack:

    def GetLocal(self, depth: uintptr_t, index: uintptr_t): ...

    def GetLocalByName(self, depth: uintptr_t, name: Str): ...

    def GetLocalByName_s(self, depth: uintptr_t, name: utf_string): ...

    def GetCode(self, depth: uintptr_t) -> Code: ...

    def Get() -> Self:
        "Gets the frame stack for the currently executing thread"


@namespace
class Eval:

    class SourceKind(Enum):
        Expr = 0
        File = 1
        Single = 2

    def Compile(src, filename, kind: SourceKind) -> Code: ...

    def Compile_s(src: utf_string, filename: utf_string, kind: SourceKind) -> Code: ...

    def Eval(code: Code, globals: Dict, locals: Dict): ...


del Enum, Dict, Str
