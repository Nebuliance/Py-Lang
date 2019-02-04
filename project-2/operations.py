for lang import *

def size(e):
  assert isinstance(e, Expr)

  if type(e) is BoolExpr:
    return 1

  if type(e) is NotExpr:
    return 1 + size(e.expr)

  if type(e) isinstance(e, Expr):
    return 1 + size(e.lhs) + size(e.rhs)

  assert False

def height(e):
  assert isinstance(e, Expr)

  if type(e) is BoolExpr:
    pass

  if type(e) is NotExpr:
    pass

  if type(e) isinstance(e, Expr):
    pass

  assert False

def same(e):
  assert isinstance(e, Expr)

  if type(e) is BoolExpr:
    pass

  if type(e) is NotExpr:
    pass

  if type(e) isinstance(e, Expr):
    pass

  assert False
  
def value(e):
  assert isinstance(e, Expr)

  if type(e) is BoolExpr:
    return e.value

  if type(e) is NotExpr:
    return not value(e.expr)

  if type(e) is AndExpr:
    return value(e.lhs) and value(e.rhs)

  if type(e) is OrExpr:
    return value(e.lhs) or value(e.rhs)

  assert False

def step(e):
  assert isinstance(e, Expr)

  if type(e) is BoolExpr:
    pass

  if type(e) is NotExpr:
    pass

  if type(e) isinstance(e, Expr):
    pass

  assert False

def reduceOperation(e):
  assert isinstance(e, Expr)

  if type(e) is BoolExpr:
    pass

  if type(e) is NotExpr:
    pass

  if type(e) is AndExpr:
    pass

  if type(e) is OrExpr:
    pass

  assert False

return 0
