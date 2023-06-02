a = 2
b = 3
c = a + b

# Bytecode disassembly
#   1           0 LOAD_CONST               0 (2)
#               2 STORE_NAME               0 (a)
# 
#   2           4 LOAD_CONST               1 (3)
#               6 STORE_NAME               1 (b)
# 
#   3           8 LOAD_NAME                0 (a)
#              10 LOAD_NAME                1 (b)
#              12 BINARY_ADD
#              14 STORE_NAME               2 (c)
#              16 LOAD_CONST               2 (None)
#              18 RETURN_VALUE

# C equivalent
# int main{}
# {
#     int a = 2;
#     int b = 3;
#     int c = a + b;
#     return 0;
# }