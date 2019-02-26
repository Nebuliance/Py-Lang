class Expr:
  """Defines the following language:

      e ::= true
            false
            not e1
            e1 and e2
            e1 or e2
            x       -- variables
            \x.e1  -- abstractions
            e1 e2   -- application
  """
  pass
  
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
  """Represents lambda abstractions of the form \\x.e1."""
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
    return f"({self.lhs}.{self.rhs})"
