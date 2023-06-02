# Compyle

Compyle is a project that stems from the compiler for my SiliconPython processor project. That compiler took Python code and output `.spy` format files. The current incarnation of Compyle is set up to have multiple backends, including one for C code to allow Python to be compiled to relatively performant C and then compiled using GCC, LLVM, or some other compiler to a native binary.