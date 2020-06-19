class Type:
  pass

class BoolType(Type):
  def __str__(self):
    return "Bool"

class IntType(Type):
  def __str__(self):
    return "Int"

class ArrowType(Type):
  def __init__(self, t1, t2):
    self.parm = t1
    self.ret = t2
  
  def __str__(self):
    return f"({self.lhs} -> {self.rhs}"

class FnType(Type):
  def __init__(self, parms, ret):
    self.parms = parms
    self.ret = ret

boolType = BoolType()
intType = IntType()

class Expr:
  pass

class BoolExpr(Expr):
  def __init__(self, val):
    self.val = val

  def __str__(self):
    return "true" if self.val else "false"

class AndExpr(Expr):
  def __init__(self, e1, e2):
    self.lhs = expr(e1)
    self.rhs = expr(e2)

  def __str__(self):
    return f"({self.lhs} and {self.rhs})"

class OrExpr(Expr):
  def __init__(self, e1, e2):
    self.lhs = expr(e1)
    self.rhs = expr(e2)

  def __str__(self):
    return f"({self.lhs} or {self.rhs})"

class NotExpr(Expr):
  def __init__(self, e1):
    self.expr = expr(e1)

  def __str__(self):
    return f"(not {self.expr})"

class IfExpr(Expr):
  def __init__(self, e1, e2, e3):
    self.cond = expr(e1)
    self.true = expr(e2)
    self.false = expr(e3)

  def __str__(self):
    return f"(if {self.cond} then {self.true} else {self.false})"

class IdExpr(Expr):
  def __init__(self, x):
    if type(x) is str:
      self.id = x
      self.ref = None
    elif type(x) is VarDecl:
      self.id = x.id
      self.ref = x

  def __str__(self):
    return self.id

class VarDecl:
  def __init__(self, id, t):
    self.id = id
    self.type = t

  def __str__(self):
    return self.id

class AbsExpr(Expr):
  def __init__(self, var, e1):
    self.var = decl(var)
    self.expr = expr(e1)

  def __str__(self):
    return f"\\{self.var}.{self.expr}"

class AppExpr(Expr):
  def __init__(self, e1, e2):
    self.lhs = expr(e1)
    self.rhs = expr(e2)

  def __str__(self):
    return f"({self.lhs} {self.rhs})"

class LambdaExpr(Expr):
  def __init__(self, vars, e1):
    self.vars = list(map(decl, vars))
    self.expr = expr(e1)

  def __str__(self):
    parms = ",".join(str(v) for v in self.vars)
    return f"\\({parms}).{self.expr}"

class CallExpr(Expr):
  def __init__(self, fn, args):
    self.fn = expr(fn)
    self.args = list(map(expr, args))

  def __str__(self):
    args = ",".join(str(a) for a in self.args)
    return f"{self.fn} ({args})"

class PlaceholderExpr(Expr):
  def __str__(self):
    return "_"

from lookup import *
from subst import *
from reduce import *
from evaluate import *
from step import *