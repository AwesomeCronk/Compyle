
# Delete top item on simulated data stack
def POP_TOP(self):
    simStack.pop()

# Move TOS0 down 1 place
def ROT_TWO(self):
    simStack.insert(-1, simStack.pop())

# Move TOS0 down 2 places
def ROT_THREE(self):
    simStack.insert(-2, simStack.pop())

# Dupicate TOS0
def DUP_TOP(self):
    simStack.append(simStack[-1])

# Duplicate TOS1 and TOS0, keeping their order
def DUP_TOP_TWO(self):
    simStack.append(simStack[-2])
    simStack.append(simStack[-2])

# Move TOS0 down 3 places
def ROT_FOUR(self):
    simStack.insert(-3, simStack.pop())
