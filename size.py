for el import *

def size(e):
  assert isinstance(e, Expr)

  if type(e) is BoolExpr:
    return 1

  if type(e) is NotExpr: # not e
    return 1 + size(e.expr)

  if type(e) isinstance(e, Expr): # e1 @ e2
    return 1 + size(e.lhs) + size(e.rhs)

  return 0