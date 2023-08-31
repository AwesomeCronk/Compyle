from ..dataTypes import *


# Do nothing
def NOP(self, instr):
    pass

def GET_AITER(self, instr):
    raise NotImplementedError('Opcode GET_AITER not implemented')

def GET_ANEXT(self, instr):
    raise NotImplementedError('Opcode GET_ANEXT not implemented')

def BEFORE_ASYNC_WITH(self, instr):
    raise NotImplementedError('Opcode BEFORE_ASYNC_WITH not implemented')

def BEGIN_FINALLY(self, instr):
    raise NotImplementedError('Opcode BEGIN_FINALLY not implemented')

def END_ASYNC_FOR(self, instr):
    raise NotImplementedError('Opcode END_ASYNC_FOR not implemented')

def STORE_SUBSCR(self, instr):
    raise NotImplementedError('Opcode STORE_SUBSCR not implemented')

def DELETE_SUBSCR(self, instr):
    raise NotImplementedError('Opcode DELETE_SUBSCR not implemented')

def GET_ITER(self, instr):
    raise NotImplementedError('Opcode GET_ITER not implemented')

def GET_YIELD_FROM_ITER(self, instr):
    raise NotImplementedError('Opcode GET_YIELD_FROM_ITER not implemented')

def PRINT_EXPR(self, instr):
    raise NotImplementedError('Opcode PRINT_EXPR not implemented')

def LOAD_BUILD_CLASS(self, instr):
    raise NotImplementedError('Opcode LOAD_BUILD_CLASS not implemented')

def YIELD_FROM(self, instr):
    raise NotImplementedError('Opcode YIELD_FROM not implemented')

def GET_AWAITABLE(self, instr):
    raise NotImplementedError('Opcode GET_AWAITABLE not implemented')

def WITH_CLEANUP_START(self, instr):
    raise NotImplementedError('Opcode WITH_CLEANUP_START not implemented')

def WITH_CLEANUP_FINISH(self, instr):
    raise NotImplementedError('Opcode WITH_CLEANUP_FINISH not implemented')

def RETURN_VALUE(self, instr):
    value = self.simStack.pop()

    # endOfProgram = instrNum == len(instrs) - 1
    # if endOfProgram: endOfProgram = endOfProgram and isinstance(value, constant)
    # if endOfProgram: endOfProgram = endOfProgram and value.knownType is NoneType
    # 
    # if endOfProgram:
    #     self.program.code.append('    return 0;')
    # else:
    self.program.code.append('    return {};'.format(value.representation))

def IMPORT_STAR(self, instr):
    raise NotImplementedError('Opcode IMPORT_STAR not implemented')

def SETUP_ANNOTATIONS(self, instr):
    raise NotImplementedError('Opcode SETUP_ANNOTATIONS not implemented')

def YIELD_VALUE(self, instr):
    raise NotImplementedError('Opcode YIELD_VALUE not implemented')

def POP_BLOCK(self, instr):
    raise NotImplementedError('Opcode POP_BLOCK not implemented')

def END_FINALLY(self, instr):
    raise NotImplementedError('Opcode END_FINALLY not implemented')

def POP_EXCEPT(self, instr):
    raise NotImplementedError('Opcode POP_EXCEPT not implemented')

# Associate a name with TOS0
def STORE_NAME(self, instr):
    name = self.codeObject.co_names[instr.arg]
    value = self.simStack.pop()
    
    self.program.code.append('    int {} = {};'.format(name, value.representation))

    value.representation = name
    self.nameMap[name] = value
    

def DELETE_NAME(self, instr):
    raise NotImplementedError('Opcode DELETE_NAME not implemented')

def UNPACK_SEQUENCE(self, instr):
    raise NotImplementedError('Opcode UNPACK_SEQUENCE not implemented')

def FOR_ITER(self, instr):
    raise NotImplementedError('Opcode FOR_ITER not implemented')

def UNPACK_EX(self, instr):
    raise NotImplementedError('Opcode UNPACK_EX not implemented')

def STORE_ATTR(self, instr):
    raise NotImplementedError('Opcode STORE_ATTR not implemented')

def DELETE_ATTR(self, instr):
    raise NotImplementedError('Opcode DELETE_ATTR not implemented')

def STORE_GLOBAL(self, instr):
    raise NotImplementedError('Opcode STORE_GLOBAL not implemented')

def DELETE_GLOBAL(self, instr):
    raise NotImplementedError('Opcode DELETE_GLOBAL not implemented')

# Load a constant value onto the stack
def LOAD_CONST(self, instr):
    const = self.codeObject.co_consts[instr.arg]
    self.log.debug('Constant is {}'.format(const))
    self.simStack.append(constant(type(const), const))

# Load an object associated with a name onto the stack
def LOAD_NAME(self, instr):
    name = self.codeObject.co_names[instr.arg]
    value = self.nameMap[name]
    self.simStack.append(value)

def LOAD_ATTR(self, instr):
    raise NotImplementedError('Opcode LOAD_ATTR not implemented')

def COMPARE_OP(self, instr):
    raise NotImplementedError('Opcode COMPARE_OP not implemented')

def IMPORT_NAME(self, instr):
    raise NotImplementedError('Opcode IMPORT_NAME not implemented')

def IMPORT_FROM(self, instr):
    raise NotImplementedError('Opcode IMPORT_FROM not implemented')

def JUMP_FORWARD(self, instr):
    raise NotImplementedError('Opcode JUMP_FORWARD not implemented')

def JUMP_IF_FALSE_OR_POP(self, instr):
    raise NotImplementedError('Opcode JUMP_IF_FALSE_OR_POP not implemented')

def JUMP_IF_TRUE_OR_POP(self, instr):
    raise NotImplementedError('Opcode JUMP_IF_TRUE_OR_POP not implemented')

def JUMP_ABSOLUTE(self, instr):
    raise NotImplementedError('Opcode JUMP_ABSOLUTE not implemented')

def POP_JUMP_IF_FALSE(self, instr):
    raise NotImplementedError('Opcode POP_JUMP_IF_FALSE not implemented')

def POP_JUMP_IF_TRUE(self, instr):
    raise NotImplementedError('Opcode POP_JUMP_IF_TRUE not implemented')

def LOAD_GLOBAL(self, instr):
    raise NotImplementedError('Opcode LOAD_GLOBAL not implemented')

def SETUP_FINALLY(self, instr):
    raise NotImplementedError('Opcode SETUP_FINALLY not implemented')

def LOAD_FAST(self, instr):
    raise NotImplementedError('Opcode LOAD_FAST not implemented')

def STORE_FAST(self, instr):
    raise NotImplementedError('Opcode STORE_FAST not implemented')

def DELETE_FAST(self, instr):
    raise NotImplementedError('Opcode DELETE_FAST not implemented')

def RAISE_VARARGS(self, instr):
    raise NotImplementedError('Opcode RAISE_VARARGS not implemented')

def CALL_FUNCTION(self, instr):
    raise NotImplementedError('Opcode CALL_FUNCTION not implemented')

def MAKE_FUNCTION(self, instr):
    raise NotImplementedError('Opcode MAKE_FUNCTION not implemented')

def LOAD_CLOSURE(self, instr):
    raise NotImplementedError('Opcode LOAD_CLOSURE not implemented')

def LOAD_DEREF(self, instr):
    raise NotImplementedError('Opcode LOAD_DEREF not implemented')

def STORE_DEREF(self, instr):
    raise NotImplementedError('Opcode STORE_DEREF not implemented')

def DELETE_DEREF(self, instr):
    raise NotImplementedError('Opcode DELETE_DEREF not implemented')

def CALL_FUNCTION_KW(self, instr):
    raise NotImplementedError('Opcode CALL_FUNCTION_KW not implemented')

def CALL_FUNCTION_EX(self, instr):
    raise NotImplementedError('Opcode CALL_FUNCTION_EX not implemented')

def SETUP_WITH(self, instr):
    raise NotImplementedError('Opcode SETUP_WITH not implemented')

def EXTENDED_ARG(self, instr):
    raise NotImplementedError('Opcode EXTENDED_ARG not implemented')

def LIST_APPEND(self, instr):
    raise NotImplementedError('Opcode LIST_APPEND not implemented')

def SET_ADD(self, instr):
    raise NotImplementedError('Opcode SET_ADD not implemented')

def MAP_ADD(self, instr):
    raise NotImplementedError('Opcode MAP_ADD not implemented')

def LOAD_CLASSDEREF(self, instr):
    raise NotImplementedError('Opcode LOAD_CLASSDEREF not implemented')

def SETUP_ASYNC_WITH(self, instr):
    raise NotImplementedError('Opcode SETUP_ASYNC_WITH not implemented')

def FORMAT_VALUE(self, instr):
    raise NotImplementedError('Opcode FORMAT_VALUE not implemented')

def LOAD_METHOD(self, instr):
    raise NotImplementedError('Opcode LOAD_METHOD not implemented')

def CALL_METHOD(self, instr):
    raise NotImplementedError('Opcode CALL_METHOD not implemented')

def CALL_FINALLY(self, instr):
    raise NotImplementedError('Opcode CALL_FINALLY not implemented')

def POP_FINALLY(self, instr):
    raise NotImplementedError('Opcode POP_FINALLY not implemented')
