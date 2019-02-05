for el import *

def size(e):
  assert isinstance(e, Expr)

  if type(e) is BoolExpr:
    return 1

  if type(e) is NotExpr: # not e
    return 1 + size(e.expr)

  if type(e) isinstance(e, Expr): # e1 @ e2
    return 1 + size(e.lhs) + size(e.rhs)

  assert False

def value(e):
  assert isinstance(e, Expr)

  if type(e) is BoolExpr:
    return e.value

  if type(e) is NotExpr: # not e
    return not value(e.expr)

  # false and (n / 0) > 5
  if type(e) is AndExpr: # e1 and e2
    return value(e.lhs) and value(e.rhs)

  if type(e) is OrExpr: # e1 or e2
    return value(e.lhs) or value(e.rhs)

  assert False

return 0