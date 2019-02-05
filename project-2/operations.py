from lang import *

"""compute size of expression"""
def size(e):
  assert isinstance(e, Expr)

  if type(e) is BoolExpr:
    return 1

  if type(e) is NotExpr:
    return 1 + size(e.expr)

  if type(e) isinstance(e, Expr):
    return 1 + size(e.lhs) + size(e.rhs)

  assert False

"""compute height of expression"""
def height(e):
  assert isinstance(e, Expr)

  if type(e) is BoolExpr:
    return 1

  if type(e) is NotExpr:
    return 1 + height(e.expr)

  if type(e) isinstance(e, Expr):
    return 1 + height(e.lhs) + height(e.rhs) 

  assert False

"""true if two expressions are identical"""
def same(e):
  assert isinstance(e, Expr)

  if type(e) is BoolExpr:
    return False

  if type(e) is NotExpr:
    return False

  if type(e) isinstance(e, Expr):
    return True if (same(e.lhs) == same(e.rhs)) else False

  assert False

"""compute value of expression"""
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

"""return expression represeting single step of evaluation"""
def step(e):
  assert isinstance(e, Expr)

  if type(e) is BoolExpr:
    pass

  if type(e) is NotExpr:
    pass

  if type(e) isinstance(e, Expr):
    pass

  assert False


"""calls repeatedly until expression is non-reducible"""
def reduceExpr(e):
  assert isinstance(e, Expr)

  if type(e) is BoolExpr:
    return e.reduceExpr

  if type(e) is NotExpr:
    return not reduceExpr(e.expr)

  if type(e) is AndExpr:
    return True if (reduceExpr(e.lhs) == True and reduceExpr(e.rhs) == True) else False

  if type(e) is OrExpr:
    eturn True if (reduceExpr(e.lhs) == True or reduceExpr(e.rhs) == True) else False

  assert False