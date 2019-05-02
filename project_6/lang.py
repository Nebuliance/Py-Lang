from classes import *

def expr(x):
  if type(x) is bool:
    return BoolExpr(x)
  if type(x) is str:
    return IdExpr(x)
  return x

def decl(x):
  if type(x) is str:
    return VarDecl(x)
  return x
