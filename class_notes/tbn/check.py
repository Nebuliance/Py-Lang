from lang import *

# Implements the typing relation e : T
# is to say that every expression e has some type
# T. If not, to say the expression is ill-typed (or
# sometimes ill-formed).

# The (only) boolean type.
boolType = BoolType()

# The (only) integer type.
intType = IntType()

def is_bool(x):
  if isinstance(x, Type):
    return x == boolType
  if isinstance(x, Expr):
    return is_bool(check(x))

def is_int():
  pass

def check_bool(e):
  # -------- T-bool
  # b : Bool
  return boolType

def check_int(e)
  # -------- T-int
  # n : int
  return intType

def check_and(e):
  # e1 : Bool   e2 : Bool
  #----------------------- T-and
  # e1 and e2 : Bool
  t1 = check(e1)
  t2 = check(e2)

  if is_bool(e1) and is_bool(e2):
    return boolType

  raise Exception("invalid operands to 'and'")


def do_check(e):
  # Compute the type of e.
  assert isinstance(e, Expr)
  assert is_reducible(e)

  if type(e) is BoolExpr:
    return check_bool(e)

  if type(e) is AndExpr:
    return check_and(e)

  if type(e) is OrExpr:
    return check_or(e)

  if type(e) is NotExpr:
    return check_not(e)

  if type(e) is IfExpr:
    return check_if(e)

  if type(e) is AddExpr:
    return check_add(e)

  if type(e) is SubExpr:
    return check_sub(e)

  if type(e) is MulExpr:
    return check_sub(e)

  if type(e) is DivExpr:
    return check_sub(e)

  if type(e) is RemExpr:
    return check_sub(e)

  if type(e) is NegExpr:
    return check_sub(e)

  if type(e) is EqExpr:
    return check_sub(e)

  if type(e) is NeExpr:
    return check_sub(e)

  if type(e) is LtExpr:
    return check_sub(e)

  if type(e) is GtExpr:
    return check_sub(e)

  if type(e) is LeExpr:
    return check_sub(e)

  if type(e) is GeExpr:
    return check_sub(e)

  assert False

def check(e):
  # Accepts an expression and returns its type.

  # If we've computed the type already, return it.
  if e.type:
    return e.type

  e.type = do_check(e)

  return e.type