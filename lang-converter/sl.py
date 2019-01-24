# JVM-like language for propositional calculus (i.e., basic logic)
#
# A program consists of a sequence of instructions.
#
# An instruction is one of:
#
# i ::= push true
#       push false
#       pop
#       and
#       or
#       not

# A value is one of True or False

class Instr:
  pass

class Push(Instr):
  def __init__(self, val):
    self.value = val

class Pop(Instr):
  pass

class And(Instr):
  pass

class Or(Instr):
  pass

class Not(Instr):
  pass

def run(prog):
  stack = []
  for ip in range(len(prog)):
    insn = prog[ip]
    if type(insn) is Push:
      stack.append(i.value)

    if type(insn) is Pop:
      stack.pop()

    if type(insn) is And:
      v1 = stack.pop()
      v2 = stack.pop()
      stack.append(v1 and v2)

    if type(insn) is Or:
      v1 = stack.pop()
      v2 = stack.pop()
      stack.append(v1 or v2)

    if type(insn) is Not: