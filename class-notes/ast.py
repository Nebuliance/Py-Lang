class Expr:
  pass

class IdExpr(Expr):
  pass

class VarDecl(Expr):
  pass

class AppExpr(Expr):
  pass

class AbsExpr(Expr):
  def __init__(self, var, e1):
    self.var = var
    self.e1 = e1

  def __str__(self):
    return f"//{self.var}.{self.e1}"

def isValue(e):
  return type(e) in (IdExpr, AbsExpr)

def isReducible(e):
  return not isValue(e)

def resolve(e, scope = []):
  if type(e) is AppExpr:
    resolve(e.lhs, scope)
    resolve(e.rhs, scope)

  if type(e) is AbsExpr:
    # \x.e -- Add x to scope, recurse through e
    
    # (\x.e) x
    resolve(e.expr, scope + [e.var])
    return

  if type(e) is IdExpr:
    for var in reversed(scope):
      if e.id == var.id:
        e.ref = var # bind id to declaration
        return
    raise Exception("name lookup error")
         
def subst(e, s):
  # s [x->v]x = v
  # [x->v]y = y (y != x)

  if type(e) is IdExpr:
    if e.id in s: # FIXME: This is wrong
      return s[e.ref]
    else:
      return e

  # [x->v] \x.e1 = \x.[x->v]e1
  if type(e) is AbsExpr:
    return AbsExpr(e.var, subst(e.expr, s))

  if type(e) is AppExpr:
    return AppExpr(
      subst(e.lhs, s),
      subst(e.rhs, s)
    )

def stepApp(e):
  """
     e1 ~> e1'
  --------------- App-1
  e1 e2 ~> e1' e2

        e2 ~> e2'
  --------------------- App-2
  \x.e1 e2 ~> \x.e1 e2'

  ------------------- App-3
  \x.e1 v ~> [x->v]e1
  """
  if isReducible(e.lhs): # App-1
    return AppExpr(step(e.lhs), e.rhs)

  if type(e.lhs) is not AbsExpr:
    raise Exception("application of non-lambda")

  if isReducible(e.rhs): # App-2
    return AppExpr(e.lhs, step(e.rhs))

  s = {e.lhs.var: e.rhs}
  return subst(e.lhs.expr, s)

def step(e):
  assert isinstance(e, Expr)
  assert isReducible(e)

  if type(e) is AppExpr:
    return stepApp(e)

  assert False