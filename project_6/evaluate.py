from eval import *

def evaluate(e, store = {}):
  if type(e) is BoolExpr:
    return eval_bool(e, store)

  if type(e) is AndExpr:
    return eval_and(e, store)

  if type(e) is OrExpr:
    return eval_or(e, store)

  if type(e) is NotExpr:
    return eval_not(e, store)

  if type(e) is IdExpr:
    return eval_id(e, store)

  if type(e) is AbsExpr:
    return eval_abs(e, store)

  if type(e) is AppExpr:
    return eval_app(e, store)

  if type(e) is LambdaExpr:
    return eval_lambda(e, store)

  if type(e) is CallExpr:
    return eval_call(e, store)
