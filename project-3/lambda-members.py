from lang import *

def lambdaValue(e):
  return type(e) in (IdExpr, AbsExpr)

def lambdaReducible(e):
  return not lambdaValue(e)

def resolve(e, scope = []):
  if type(e) is AppExpr:
    resolve(e.lhs, scope)
    resolve(e.rhs, scope)
    return

  if type(e) is AbsExpr:
    resolve(e.expr, scope + [e.var])
    return

  if type(e) is IdExpr:
    for var in reversed(scope):
      if e.id == var.id:
        e.ref = var
        return
    raise Exception("name lookup error")

  assert False

def subst(e, s):
  if type(e) is IdExpr:
    if e.ref in s:
      return s[e.ref]
    else:
      return e

  if type(e) is AbsExpr:
    return AbsExpr(e.var, subst(e.expr, s))

  if type(e) is AppExpr:
    return AppExpr(subst(e.lhs, s), subst(e.rhs, s))

  assert False

def appStep(e):
  if lambdaReducible(e.lhs):
    return AppExpr(lambdaStep(e.lhs), e.rhs)

  if type(e.lhs) is not AbsExpr:
    raise Exception("application of non-lambda")

  if lambdaReducible(e.rhs):
    return AppExpr(e.lhs, lambdaStep(e.rhs))

  s = {e.lhs.var: e.rhs}
  return subst(e.lhs.expr, s)

def lambdaStep(e):
  assert isinstance(e, Expr)
  assert lambdaReducible(e)

  if type(e) is AppExpr:
    return appStep(e)

  assert False