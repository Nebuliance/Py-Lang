from lang import *
from classes import *
from lookup import *

import copy

clone = copy.deepcopy

class Closure:
  def __init__(self, abs, env):
    self.abs = abs
    self.env = clone(env)

def eval_bool(e, store):
  return e.val

def eval_and(e, store):
  return evaluate(e.lhs, store) and evaluate(e.rhs, store)

def eval_or(e, store):
  return evaluate(e.lhs, store) or evaluate(e.rhs, store)

def eval_not(e, store):
  return not evaluate(e.expr, store)

def eval_cond(e, store):
  if evaluate(e.cond):
    return evaluate(e.true)
  else:
    return evaluate(e.false)

def eval_id(e, store):
  return store[e.ref]

def eval_abs(e, store):
  return Closure(e, store)

def eval_app(e, store):
  c = evaluate(e.lhs, store)

  if type(c) is not Closure:
    raise Exception("cannot apply non-closure to an argument")

  v = evaluate(e.rhs, store)

  return evaluate(c.abs.expr, c.env + {c.abs.var: v})

def eval_lambda(e, store):
  return Closure(e, store)

def eval_call(e, store):
  c = evaluate(e.fn, store)
  
  if type(c) is not Closure:
    raise Exception("cannot apply non-closure to an argument")

  args = []
  for a in e.args:
    args += [evaluate(a, store)]

  env = clone(c.env)
  for i in range(len(args)):
    env[c.abs.vars[i]] = args[i]

  return evaluate(c.abs.expr, env)
