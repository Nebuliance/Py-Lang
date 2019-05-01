from lang import *
from bm import *
from im import *
from reduce import *
from step import *
from check import *
from expression import *

def evaluate(e):
  assert isinstance(e, Expr)

  if type(e) is BoolExpr:
    return boolEval(e)

  if type(e) is AndExpr:
    return andEval(e)

  if type(e) is OrExpr:
    return orEval(e)

  if type(e) is NotExpr:
    return notEval(e)

  if type(e) is IfExpr:
    return ifEval(e)

  if type(e) is IntExpr:
    return intEval(e)

  if type(e) is AddExpr:
    return addEval(e)

  if type(e) is SubExpr:
    return subEval(e)

  if type(e) is MulExpr:
    return mulEval(e)

  if type(e) is DivExpr:
    return divEval(e)

  if type(e) is RemExpr:
    return remEval(e)

  if type(e) is NegExpr:
    return negEval(e)

  if type(e) is EqExpr:
    return eqEval(e)

  if type(e) is NeExpr:
    return neEval(e)

  if type(e) is LtExpr:
    return ltEval(e)

  if type(e) is GtExpr:
    return gtEval(e)

  if type(e) is LeExpr:
    return leEval(e)

  if type(e) is GeExpr:
    return geEval(e)

  assert False
