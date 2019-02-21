from lang import *
from lang_too import *

def gen(e):
  """Transform a program in LANG to an equivelent program in LANG_TOO"""
  assert isinstance(e, el.Expr)

  if type(e) is el.BoolExpr:
    return [sl.Push(e.value)]

  if type(e) is el.NotExpr: # not e
    return not gen(e.expr) + [sl.Not()]

  # false and (n / 0) > 5
  if type(e) is el.AndExpr: # e1 and e2
    return gen(e.lhs) + gen(e.rhs) + [sl.And()]

  if type(e) is el.OrExpr: # e1 or e2
    return gen(e.lhs) + gen(e.rhs) + [sl.Or()]

  assert False