from lang import *

"""compute size of expression"""
def size(e):
  assert isinstance(e, Expr)

  if type(e) is BoolExpr:
    return 1

  if type(e) is NotExpr:
    return 1 + size(e.expr)

  if type(e) is BinaryExpr:
    return 1 + size(e.lhs) + size(e.rhs)

  assert False

"""compute height of expression"""
def height(e):
  assert isinstance(e, Expr)

  if type(e) is BoolExpr:
    return 0

  if type(e) is NotExpr:
    return 1 + height(e.expr)

  if type(e) is BinaryExpr:
    return 1 + (height(e.lhs) and height(e.rhs))

  assert False

"""true if two expressions are identical"""
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

def isValue(e):
  return type(e) is BoolExpr

def isReducible(e):
  return not isValue(e)

def notStep(e):
  if isValue(e.expr):
    return BoolExpr(not e.expr.value)

  return NotExpr(step(e.expr))

  assert False

def andStep(e):
  if isValue(e.lhs) and isValue(e.rhs):
    return BoolExpr(e.lhs.value and e.rhs.value)

  if isReducible(e.lhs):
    return AndExpr(step(e.lhs), e.rhs)

  if isReducible(e.rhs):
    return AndExpr(e.lhs, step(e.rhs))

  assert False

def orStep(e):
  if isValue(e.lhs) and isValue(e.rhs):
    return BoolExpr(e.lhs.value or e.rhs.value)

  if isReducible(e.lhs):
    return OrExpr(step(e.lhs), e.rhs)

  if isReducible(e.rhs):
    return OrExpr(e.lhs, step(e.rhs))

  assert False

"""return expression representing single step of evaluation"""
def step(e):
  assert isReducible(e)

  if type(e) is NotExpr:
    return notStep(e)

  if type(e) is AndExpr:
    return andStep(e)

  if type(e) is OrExpr:
    return orStep(e)

  assert False

"""calls repeatedly until expression is non-reducible"""
def reduceExpr(e):
  while isReducible(e):
    e = step(e)

  return e

  assert False
