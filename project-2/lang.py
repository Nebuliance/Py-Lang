class Expr:
  """Defines the following language:

      e ::= true
            false
            not e1
            e1 and e2
            e1 or e2
  """
  
class BoolExpr(Expr):
  """Represents the strings 'true' and 'false'."""
  def __init__(self, val):
    assert val == True or val == False
    self.value = val

class NotExpr(Expr):
  """Represents strings of the form 'not e'."""
  def __init__(self, e):
    assert isinstance(e, Expr)
    self.expr = e

class BinaryExpr(Expr):
  """Represents strings of the form 'e1 @ e2'."""
  def __init__(self, e1, e2):
    
    self.lhs = e1
    self.rhs = e2

class AndExpr(BinaryExpr):
  """Represents strings of the form 'e1 and e2'."""  

class OrExpr(BinaryExpr):
  """Represents strings of the form 'e1 or e2'."""
