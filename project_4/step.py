from lang import *
from bm import *
from im import *
from reduce import *
from evaluate import *
from check import *
from expression import *

def unaryStep(e, Node, op):
  if isReducible(e.expr):
    return Node(step(e.expr))

  return expr(op(e.expr.value))

def binaryStep(e, Node, op):
  if isReducible(e.lhs):
    return Node(step(e.lhs), e.rhs)

  if isReducible(e.rhs):
    return Node(e.lhs, step(e.rhs))

  return expr(op(e.lhs.value, e.rhs.value))

def step(e):
  assert isinstance(e, Expr)
  assert isReducible(e)

  if type(e) is AndExpr:
    return andStep(e)

  if type(e) is OrExpr:
    return orStep(e)

  if type(e) is NotExpr:
    return notStep(e)

  if type(e) is IfExpr:
    return ifStep(e)

  if type(e) is AddExpr:
    return addStep(e)

  if type(e) is SubExpr:
    return subStep(e)

  if type(e) is MulExpr:
    return mulStep(e)

  if type(e) is DivExpr:
    return divStep(e)

  if type(e) is RemExpr:
    return remStep(e)

  if type(e) is NegExpr:
    return neStep(e)

  if type(e) is EqExpr:
    return eqStep(e)

  if type(e) is NeExpr:
    return neStep(e)

  if type(e) is LtExpr:
    return ltStep(e)

  if type(e) is GtExpr:
    return gtStep(e)

  if type(e) is LeExpr:
    return leStep(e)

  if type(e) is GeExpr:
    return geStep(e)

  assert False