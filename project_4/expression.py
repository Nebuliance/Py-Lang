from lang import *
from bm import *
from im import *
from evaluate import *
from reduce import *
from check import *
from step import *

boolType = BoolType()

intType = IntType()

def isBool(x):
  if isinstance(x, Type):
    return x == boolType

  if isinstance(x, Expr):
    return isBool(check(x))

def isInt(x):
  if isinstance(x, Type):
    return x == intType

  if isinstance(x, Expr):
    return isInt(check(x))

def isSameType(t1, t2):
  if type(t1) is not type(t2):
    return False

  if type(t1) is BoolType:
    return True
  
  if type(t1) is IntType:
    return True

  assert False

def hasSameType(e1, e2):
  return isSameType(check(e1), check(e2))




def expr(x):
  if type(x) is bool:
    return BoolExpr(x)

  if type(x) is int:
    return IntExpr(x)

  if type(x) is str:
    return IdExpr(x)

  return x
