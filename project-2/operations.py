from lang import *

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
    return 1

  if type(e) is NotExpr:
    return 1 + height(e.height)

  if type(e) isinstance(e, Expr):
    return 1 + height(e.lhs) + height(e.rhs) 

  assert False

def same(e):
  assert isinstance(e, Expr)

  if type(e) is BoolExpr:
    return e.same

  if type(e) is NotExpr:
    return not same(e.expr)

  if type(e) isinstance(e, Expr):
    return True if (e.lhs == e.rhs) else False

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
    return 0

  if type(e) is NotExpr:
    return 1

  if type(e) isinstance(e, Expr):
    return 1

  assert False

def reduceOperation(e):
  assert isinstance(e, Expr)

  if type(e) is BoolExpr:
    return e.reduceOperation

  if type(e) is NotExpr:
    return not reduceOperation(e.expr)

  if type(e) is AndExpr:
    pass

  if type(e) is OrExpr:
    pass

  assert False