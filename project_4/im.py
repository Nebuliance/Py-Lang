from lang import *
from bm import *
from reduce import *
from evaluate import *
from step import *
from check import *
from expression import *

def intEval(e):
  return e.value

def addEval(e):
  return evaluate(e.lhs) + evaluate(e.rhs)

def subEval(e):
  return evaluate(e.lhs) - evaluate(e.rhs)

def mulEval(e):
  return evaluate(e.lhs) * evaluate(e.rhs)

def divEval(e):
  return evaluate(e.lhs) / evaluate(e.rhs)

def remEval(e):
  return evaluate(e.lhs) % evaluate(e.rhs)

def negEval(e):
  return -evaluate(e.expr)

def eqEval(e):
  return evaluate(e.lhs) == evaluate(e.rhs)

def neEval(e):
  return evaluate(e.lhs) != evaluate(e.rhs)

def ltEval(e):
  return evaluate(e.lhs) < evaluate(e.rhs)

def gtEval(e):
  return evaluate(e.lhs) > evaluate(e.rhs)

def leEval(e):
  return evaluate(e.lhs) <= evaluate(e.rhs)

def geEval(e):
  return evaluate(e.lhs) >= evaluate(e.rhs)





def addStep(e):
  return binaryStep(e, AddExpr, lambda x, y: x + y)

def subStep(e):
  return binaryStep(e, SubExpr, lambda x, y: x - y)

def mulStep(e):
  return binaryStep(e, MulExpr, lambda x, y: x * y)

def divStep(e):
  return binaryStep(e, DivExpr, lambda x, y: x / y)

def remStep(e):
  return binaryStep(e, RemExpr, lambda x, y: x % y)

def eqStep(e):
  return binaryStep(e, EqExpr, lambda x, y: x == y)

def neStep(e):
  return binaryStep(e, NeExpr, lambda x, y: x != y)

def ltStep(e):
  return binaryStep(e, LtExpr, lambda x, y: x < y)

def gtStep(e):
  return binaryStep(e, GtExpr, lambda x, y: x > y)

def leStep(e):
  return binaryStep(e, LeExpr, lambda x, y: x <= y)

def geStep(e):
  return binaryStep(e, GeExpr, lambda x, y: x >= y)




def addCheck(e):
  if isInt(e.lhs) and isInt(e.rhs):
    return intType

  raise Exception("invalid operands to '+'")

def subCheck(e):
  if isInt(e.lhs) and isInt(e.rhs):
    return intType

  raise Exception("invalid operands to '-'")

def eqCheck(e):
  if hasSameType(e.lhs, e.rhs):
    return boolType

  raise Exception("invalid operands to '=='")
