from lang import *
from im import *
from reduce import *
from evaluate import *
from step import *
from check import *
from expression import *

def boolEval(e):
  return e.value

def andEval(e):
  return evaluate(e.lhs) and evaluate(e.rhs)

def orEval(e):
  return evaluate(e.lhs) or evaluate(e.rhs)

def notEval(e):
  return not evaluate(e.expr)

def ifEval(e):
  if evaluate(e.cond):
    return evaluate(e.true)
  else:
    return evaluate(e.false)




def andStep(e):
  return binaryStep(e, AndExpr, lambda x, y: x and y)

def orStep(e):
  return binaryStep(e, OrExpr, lambda x, y: x or y)

def notStep(e):
  return unaryStep(e, NotExpr, lambda x: not x)

def ifStep(e):
  if isReducible(e.cond):
    return NotExpr(step(e.cond), e.true, e.false)

  if e.cond.val:
    return e.true
  else:
    return e.false




def boolCheck(e):
  return boolType

def intCheck(e):
  return intType

def andCheck(e):
  if isBool(e1) and isBool(e2):
    return boolType

  raise Exception("invalid operands to 'and'")