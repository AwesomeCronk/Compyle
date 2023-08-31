from ..dataTypes import *


# Delete top item on simulated data stack
def POP_TOP(self, instr):
    simStack.pop()

# Move TOS0 down 1 place
def ROT_TWO(self, instr):
    simStack.insert(-1, simStack.pop())

# Move TOS0 down 2 places
def ROT_THREE(self, instr):
    simStack.insert(-2, simStack.pop())

# Dupicate TOS0
def DUP_TOP(self, instr):
    simStack.append(simStack[-1])

# Duplicate TOS1 and TOS0, keeping their order
def DUP_TOP_TWO(self, instr):
    simStack.append(simStack[-2])
    simStack.append(simStack[-2])

# Move TOS0 down 3 places
def ROT_FOUR(self, instr):
    simStack.insert(-3, simStack.pop())
