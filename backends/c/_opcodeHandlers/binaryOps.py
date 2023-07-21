from backends.c import constant, variable


def BINARY_MATRIX_MULTIPLY(self):
    raise NotImplementedError('Opcode BINARY_MATRIX_MULTIPLY not implemented')

def INPLACE_MATRIX_MULTIPLY(self):
    raise NotImplementedError('Opcode INPLACE_MATRIX_MULTIPLY not implemented')

def BINARY_POWER(self):
    raise NotImplementedError('Opcode BINARY_POWER not implemented')

def BINARY_MULTIPLY(self):
    raise NotImplementedError('Opcode BINARY_MULTIPLY not implemented')

def BINARY_MODULO(self):
    raise NotImplementedError('Opcode BINARY_MODULO not implemented')

def BINARY_ADD(self):
    a = self.simStack.pop()
    b = self.simStack.pop()

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

def BINARY_SUBTRACT(self):
    raise NotImplementedError('Opcode BINARY_SUBTRACT not implemented')

def BINARY_SUBSCR(self):
    raise NotImplementedError('Opcode BINARY_SUBSCR not implemented')

def BINARY_FLOOR_DIVIDE(self):
    raise NotImplementedError('Opcode BINARY_FLOOR_DIVIDE not implemented')

def BINARY_TRUE_DIVIDE(self):
    raise NotImplementedError('Opcode BINARY_TRUE_DIVIDE not implemented')

def BINARY_LSHIFT(self):
    raise NotImplementedError('Opcode BINARY_LSHIFT not implemented')

def BINARY_RSHIFT(self):
    raise NotImplementedError('Opcode BINARY_RSHIFT not implemented')

def BINARY_AND(self):
    raise NotImplementedError('Opcode BINARY_AND not implemented')

def BINARY_XOR(self):
    raise NotImplementedError('Opcode BINARY_XOR not implemented')

def BINARY_OR(self):
    raise NotImplementedError('Opcode BINARY_OR not implemented')
