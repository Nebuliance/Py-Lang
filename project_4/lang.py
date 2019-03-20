class Expr:
  # Represents the set of expressions in the
  # pure (or untyped) lambda calculus. This is
  # defined as:
  #
  #   e ::= b                     -- boolean literals (true and false)
  #         e1 and e2             -- logical and
  #         e1 or e2              -- logical or
  #         not e1                -- logical negation
  #         if e1 then e2 else e3 -- conditionals
  #         n                     -- integer literals
  #         e1 + e2               -- addition
  #         e1 - e2               -- subtraction
  #         e1 * e2               -- multiplication
  #         e1 / e2               -- quotient of division
  #         e1 % e2               -- remainder of division
  #         -e1                   -- negation
  #         e1 == e2              -- equality
  #         e1 != e2              -- distinction
  #         e1 < e2               -- less than
  #         e1 > e2               -- greater than
  #         e1 <= e2              -- less than or equal to
  #         e1 >= e2              -- greater than or equal to
  def __init__(self):
    # The type of the expression. This is computed 
    # by the check() function.
    self.type = None
  
class BoolExpr(Expr):
  """Represents the strings 'true' and 'false'."""
  def __init__(self, val):
    assert val == True or val == False
    self.value = val

class NotExpr(Expr):
  """Represents strings of the form 'not e'."""
  def __init__(self, e):
    self.expr = e

class AndExpr(BinaryExpr):
  """Represents strings of the form 'e1 and e2'."""
  def __init__(self, e1, e2):
    self.lhs = e1
    self.rhs = e2

class OrExpr(BinaryExpr):
  """Represents strings of the form 'e1 or e2'."""
  def __init__(self, e1, e2):
    self.lhs = e1
    self.rhs = e2

class IdExpr(Expr):
  """Represents identifiers that refer to variables."""
  def __init__(self, id):
    self.id = id
    self.ref = None

  def __str__(self):
    return self.id

class VarDecl:
  """Represents the declaration of a variable."""
  def __init__(self, id):
    self.id = id

  def __str__(self):
    return self.id

class AbsExpr(Expr):
  """Represents lambda abstractions of the form \x.e1."""
  def __init__(self, var, e1):
    if type(var) is str:
      self.var = VarDecl(var)
    else:
      self.var = var
      self.expr = e1

  def __str__(self):
    return f"\{self.var}.{self.expr}"

class AppExpr(Expr):
  """Represents application."""
  def __init__(self, lhs, rhs):
    self.lhs = lhs
    self.rhs = rhs

  def __str__(self):
    return f"({self.lhs}.{self.rhs})"
