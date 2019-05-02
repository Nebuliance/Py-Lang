from step import *

def is_value(e):
  return type(e) in (BoolExpr, AbsExpr, LambdaExpr)

def is_reducible(e):
  return not is_value(e)

def reduce(e):
  while not is_value(e):
    e = step(e)
    print(e)
  return e
