from lang import *
from bm import *
from im import *
from evaluate import *
from step import *
from check import *
from expression import *

def isValue(e):
  return type(e) in (BoolExpr, IntExpr)

def isReducible(e):
  return not isValue(e)

def reduce(e):
  while not isValue(e):
    e = step(e)
    print(e)

  return e
