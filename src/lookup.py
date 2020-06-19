from lang import *
from classes import *

def lookup(id, stk):
  for scope in reversed(stk):
    if id in scope:
      return scope[id]
  return None