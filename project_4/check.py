from lang import *
from bm import *
from im import *
from evaluate import *
from reduce import *
from step import *
from expression import *

def doCheck(e):
  assert isinstance(e, Expr)

  if type(e) is BoolExpr:
    return boolCheck(e)

  if type(e) is AndExpr:
    return andCheck(e)

  if type(e) is OrExpr:
    return check_or(e)

  if type(e) is NotExpr:
    return check_not(e)

  if type(e) is IfExpr:
    return check_if(e)

  if type(e) is IntExpr:
    return intCheck(e)

  if type(e) is AddExpr:
    return addCheck(e)

  if type(e) is SubExpr:
    return subCheck(e)

  if type(e) is MulExpr:
    return check_mul(e)

  if type(e) is DivExpr:
    return check_div(e)

  if type(e) is RemExpr:
    return check_rem(e)

  if type(e) is NegExpr:
    return check_neg(e)

  if type(e) is EqExpr:
    return eqCheck(e)

  if type(e) is NeExpr:
    return check_ne(e)

  if type(e) is LtExpr:
    return check_lt(e)

  if type(e) is GtExpr:
    return check_gt(e)

  if type(e) is LeExpr:
    return check_le(e)

  if type(e) is GeExpr:
    return check_ge(e)

  assert False




def check(e):
  if not e.type:
    e.type = doCheck(e)

  return e.type
