class Expr:
  """
  Represents the set of expressions in the
  pure (or untyped) lambda calculus. This is
  defined as:

    e ::= x       -- variables
          \x.e1  -- abstractions
          e1 e2   -- application
  """
  pass

class IdExpr(Expr):
  """Represents identifiers that refer to
  variables."""
  def __init__(self, id):
    self.id = id
    self.ref = None

  def __str__(self):
    return self.id

class VarDecl:
  """Represents the declaration of a variable.

  Note that this is NOT an expression. It is
  the declaration of a name."""
  def __init__(self, id):
    self.id = id

  def __str__(self):
    return self.id

class AbsExpr(Expr):
  """Represents lambda abstractions of the
  form \\x.e1."""
  def __init__(self, var, e1):
    if type(var) is str:
      self.var = VarDecl(var)
    else:
      self.var = var
    self.expr = e1

  def __str__(self):
    return f"\\{self.var}.{self.expr}"

class AppExpr(Expr):
  """Represents application."""
  def __init__(self, lhs, rhs):
    self.lhs = lhs
    self.rhs = rhs

  def __str__(self):
    return f"({self.lhs} {self.rhs})"

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
    # \x.e -- Add x to scope, recurse through e
    # (\x.e) x
    resolve(e.expr, scope + [e.var])
    return

  if type(e) is IdExpr:
    for var in reversed(scope):
      if e.id == var.id:
        e.ref = var # Bind id to declaration
        return
    raise Exception("name lookup error")

  # print(type(e))
  assert False

def subst(e, s):
  # [x->v]x = v
  # [x->v]y = y (y != x)
  if type(e) is IdExpr:
    if e.ref in s: # FIXME: This is wrong.
      return s[e.ref]
    else:
      return e

  # [x->v] \x.e1 = \x.[x->v]e1
  if type(e) is AbsExpr:
    return AbsExpr(e.var, subst(e.expr, s))

  if type(e) is AppExpr:
    return AppExpr(subst(e.lhs, s), subst(e.rhs, s))

  assert False

def appStep(e):
  #
  #    e1 ~> e1'
  # --------------- App-1
  # e1 e2 ~> e1' e2
  #
  #       e2 ~> e2'
  # --------------------- App-2
  # \x.e1 e2 ~> \x.e1 e2'
  #
  # ------------------- App-3
  # \x.e1 v ~> [x->v]e1
  
  if lambdaReducible(e.lhs): # App-1
    return AppExpr(lambdaStep(e.lhs), e.rhs)

  if type(e.lhs) is not AbsExpr:
    raise Exception("application of non-lambda")

  if lambdaReducible(e.rhs): # App-2
    return AppExpr(e.lhs, lambdaStep(e.rhs))

  s = {
    e.lhs.var: e.rhs
  }
  return subst(e.lhs.expr, s);

def lambdaStep(e):
  assert isinstance(e, Expr)
  assert lambdaReducible(e)

  if type(e) is AppExpr:
    return appStep(e)

  assert False
