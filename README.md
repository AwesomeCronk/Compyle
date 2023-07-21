# Compyle

Compyle is a project that stems from the compiler for my SiliconPython processor project. That compiler took Python code and output `.spy` format files. The current incarnation of Compyle is set up to have multiple backends, including one for C code to allow Python to be compiled to relatively performant C and then compiled using GCC, LLVM, or some other compiler to a native binary.

CPython opcodes:
```
01 : POP_TOP
02 : ROT_TWO
03 : ROT_THREE
04 : DUP_TOP
05 : DUP_TOP_TWO
06 : ROT_FOUR
09 : NOP
0A : UNARY_POSITIVE
0B : UNARY_NEGATIVE
0C : UNARY_NOT
0F : UNARY_INVERT
10 : BINARY_MATRIX_MULTIPLY
11 : INPLACE_MATRIX_MULTIPLY
13 : BINARY_POWER
14 : BINARY_MULTIPLY
16 : BINARY_MODULO
17 : BINARY_ADD
18 : BINARY_SUBTRACT
19 : BINARY_SUBSCR
1A : BINARY_FLOOR_DIVIDE
1B : BINARY_TRUE_DIVIDE
1C : INPLACE_FLOOR_DIVIDE
1D : INPLACE_TRUE_DIVIDE
32 : GET_AITER
33 : GET_ANEXT
34 : BEFORE_ASYNC_WITH
35 : BEGIN_FINALLY
36 : END_ASYNC_FOR
37 : INPLACE_ADD
38 : INPLACE_SUBTRACT
39 : INPLACE_MULTIPLY
3B : INPLACE_MODULO
3C : STORE_SUBSCR
3D : DELETE_SUBSCR
3E : BINARY_LSHIFT
3F : BINARY_RSHIFT
40 : BINARY_AND
41 : BINARY_XOR
42 : BINARY_OR
43 : INPLACE_POWER
44 : GET_ITER
45 : GET_YIELD_FROM_ITER
46 : PRINT_EXPR
47 : LOAD_BUILD_CLASS
48 : YIELD_FROM
49 : GET_AWAITABLE
4B : INPLACE_LSHIFT
4C : INPLACE_RSHIFT
4D : INPLACE_AND
4E : INPLACE_XOR
4F : INPLACE_OR
51 : WITH_CLEANUP_START
52 : WITH_CLEANUP_FINISH
53 : RETURN_VALUE
54 : IMPORT_STAR
55 : SETUP_ANNOTATIONS
56 : YIELD_VALUE
57 : POP_BLOCK
58 : END_FINALLY
59 : POP_EXCEPT
5A : STORE_NAME
5B : DELETE_NAME
5C : UNPACK_SEQUENCE
5D : FOR_ITER
5E : UNPACK_EX
5F : STORE_ATTR
60 : DELETE_ATTR
61 : STORE_GLOBAL
62 : DELETE_GLOBAL
64 : LOAD_CONST
65 : LOAD_NAME
66 : BUILD_TUPLE
67 : BUILD_LIST
68 : BUILD_SET
69 : BUILD_MAP
6A : LOAD_ATTR
6B : COMPARE_OP
6C : IMPORT_NAME
6D : IMPORT_FROM
6E : JUMP_FORWARD
6F : JUMP_IF_FALSE_OR_POP
70 : JUMP_IF_TRUE_OR_POP
71 : JUMP_ABSOLUTE
72 : POP_JUMP_IF_FALSE
73 : POP_JUMP_IF_TRUE
74 : LOAD_GLOBAL
7A : SETUP_FINALLY
7C : LOAD_FAST
7D : STORE_FAST
7E : DELETE_FAST
82 : RAISE_VARARGS
83 : CALL_FUNCTION
84 : MAKE_FUNCTION
85 : BUILD_SLICE
87 : LOAD_CLOSURE
88 : LOAD_DEREF
89 : STORE_DEREF
8A : DELETE_DEREF
8D : CALL_FUNCTION_KW
8E : CALL_FUNCTION_EX
8F : SETUP_WITH
90 : EXTENDED_ARG
91 : LIST_APPEND
92 : SET_ADD
93 : MAP_ADD
94 : LOAD_CLASSDEREF
95 : BUILD_LIST_UNPACK
96 : BUILD_MAP_UNPACK
97 : BUILD_MAP_UNPACK_WITH_CALL
98 : BUILD_TUPLE_UNPACK
99 : BUILD_SET_UNPACK
9A : SETUP_ASYNC_WITH
9B : FORMAT_VALUE
9C : BUILD_CONST_KEY_MAP
9D : BUILD_STRING
9E : BUILD_TUPLE_UNPACK_WITH_CALL
A0 : LOAD_METHOD
A1 : CALL_METHOD
A2 : CALL_FINALLY
A3 : POP_FINALLY
```
