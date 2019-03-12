from lang import *

def size(e):
  assert isinstance(e, Expr)

  if type(e) is BoolExpr:
    return 1

  if type(e) is NotExpr:
    return 1 + size(e.expr)

  if type(e) is BinaryExpr:
    return 1 + size(e.lhs) + size(e.rhs)

  assert False

def height(e):
  assert isinstance(e, Expr)

  if type(e) is BoolExpr:
    return 0

  if type(e) is NotExpr:
    return 1 + height(e.expr)

  if type(e) is BinaryExpr:
    return 1 + (height(e.lhs) and height(e.rhs))

  assert False

def same(e1, e2):
  assert isinstance(e1, Expr)
  assert isinstance(e2, Expr)

  if type(e1) is not type(e2):
    return False

  if type(e1) is BoolExpr:
    return e1.value == e2.value

  if type(e1) is NotExpr:
    return same(e1.expr, e2.expr)

  if type(e1) is BinaryExpr:
    return same(e1.lhs, e2.lhs) and same(e1.rhs, e2.rhs)

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

def boolValue(e):
  return type(e) is BoolExpr

def boolReducible(e):
  return not boolValue(e)

def notStep(e):
  if boolValue(e.expr):
    return BoolExpr(not e.expr.value)

  return NotExpr(step(e.expr))

  assert False

def andStep(e):
  if boolValue(e.lhs) and boolValue(e.rhs):
    return BoolExpr(e.lhs.value and e.rhs.value)

  if boolReducible(e.lhs):
    return AndExpr(step(e.lhs), e.rhs)

  if boolReducible(e.rhs):
    return AndExpr(e.lhs, step(e.rhs))

  assert False

def orStep(e):
  if boolValue(e.lhs) and boolValue(e.rhs):
    return BoolExpr(e.lhs.value or e.rhs.value)

  if boolReducible(e.lhs):
    return OrExpr(step(e.lhs), e.rhs)

  if boolReducible(e.rhs):
    return OrExpr(e.lhs, step(e.rhs))

  assert False

def boolStep(e):
  assert boolReducible(e)

  if type(e) is NotExpr:
    return notStep(e)

  if type(e) is AndExpr:
    return andStep(e)

  if type(e) is OrExpr:
    return orStep(e)

  assert False

def reduceExpr(e):
  while boolReducible(e):
    e = step(e)

  return e

  assert False