from ..dataTypes import *


def BINARY_MATRIX_MULTIPLY(self, instr):
    raise NotImplementedError('Opcode BINARY_MATRIX_MULTIPLY not implemented')

def INPLACE_MATRIX_MULTIPLY(self, instr):
    raise NotImplementedError('Opcode INPLACE_MATRIX_MULTIPLY not implemented')

def BINARY_POWER(self, instr):
    raise NotImplementedError('Opcode BINARY_POWER not implemented')

def BINARY_MULTIPLY(self, instr):
    raise NotImplementedError('Opcode BINARY_MULTIPLY not implemented')

def BINARY_MODULO(self, instr):
    raise NotImplementedError('Opcode BINARY_MODULO not implemented')

def BINARY_ADD(self, instr):
    b = self.simStack.pop()
    a = self.simStack.pop()

    if isinstance(a, constant) and isinstance(b, constant):
        if a.knownType == b.knownType:
            result = variable([a.knownType,], '{} + {}'.format(a.representation, b.representation))
        else:
            self.log.error('BINARY_ADD with different-typed constants not implemented')
            result = variable([], '???')
    else:
        self.log.warning('BINARY_ADD with non-constants incomplete')
        result = variable([a.knownType,], '{} + {}'.format(a.representation, b.representation))

    self.simStack.append(result)

def BINARY_SUBTRACT(self, instr):
    raise NotImplementedError('Opcode BINARY_SUBTRACT not implemented')

def BINARY_SUBSCR(self, instr):
    raise NotImplementedError('Opcode BINARY_SUBSCR not implemented')

def BINARY_FLOOR_DIVIDE(self, instr):
    raise NotImplementedError('Opcode BINARY_FLOOR_DIVIDE not implemented')

def BINARY_TRUE_DIVIDE(self, instr):
    raise NotImplementedError('Opcode BINARY_TRUE_DIVIDE not implemented')

def BINARY_LSHIFT(self, instr):
    raise NotImplementedError('Opcode BINARY_LSHIFT not implemented')

def BINARY_RSHIFT(self, instr):
    raise NotImplementedError('Opcode BINARY_RSHIFT not implemented')

def BINARY_AND(self, instr):
    raise NotImplementedError('Opcode BINARY_AND not implemented')

def BINARY_XOR(self, instr):
    raise NotImplementedError('Opcode BINARY_XOR not implemented')

def BINARY_OR(self, instr):
    raise NotImplementedError('Opcode BINARY_OR not implemented')
