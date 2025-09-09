
from enum import Enum
from .support import *
from .objects import VectorCall


class CType(Enum):
    U1 = 0 # Unsigned integers (size in bytes)
    U2 = 1
    U4 = 2
    U8 = 3
    UP = 7 # Signed integers (size in bytes)
    I1 = 8
    I2 = 9
    I4 = 10
    I8 = 11
    IP = 15
    BOOL = 16 # 1 byte boolean
    F4 = 26 # 32 bit IEEE float
    F8 = 27 # 64 bit IEEE float
    GLOBAL = 34 # Index into global variable table
    POINTER = 39 # Pointer to C data. Treated as opaque by the VM.

#forward declaration:
class FieldDescriptor(Struct):
    pass

@function_pointer
def Getter(obj, field: FieldDescriptor, data: Pointer[Void]):
    "`data` points to the struct"


@function_pointer
def Setter(obj, field: FieldDescriptor, data: Pointer[Void], value) -> Void:
    "`data` points to the struct"


class FieldDescriptor(Struct):
    """ Describes a field within a struct.
    """
    name: utf_string
    doc: utf_string
    offset: uint32_t
    flags: uint16_t
    type: uint8_t # Must be one of the CType enum above.
    get: Getter # if NULL, implies the field can be read directly unless the WRITE_ONLY flag is set.
    set: Setter # if NULL, implies the field can be written directly, unless the READ_ONLY flag is set.


class StructLayout(Struct):
    """ This struct provides the means for describing
    the layout of C structs that can be understood by a
    Python VM and any associated tooling.
    Tooling will be provided to parse C structs and produce this struct."""
    name: utf_string
    fields: [FieldDescriptor] # NULL terminated array.


@namespace
class TypeSpec:
    """
        TO DO:

        This should *not* follow HPy as that follows CPython's current C API
        too closely and inherits many of its flaws.

        See https://github.com/faster-cpython/ideas/issues/553 for the general idea
        of what this API needs to support.


    """

@function_pointer
def CFunctionPointer() -> Void: ...

class FunctionDefinition(Struct):
    name: utf_string
    doc: utf_string
    signature: utf_string
    impl: CFunctionPointer
    call: VectorCall


@namespace
class Module:

    class Def(Struct):
        doc: utf_string
        state: StructLayout
        functions: [FunctionDefinition]
