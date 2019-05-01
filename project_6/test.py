from lang import *

e = EqExpr(AddExpr(3, 5), SubExpr(11, 5))

print(e)
print(check(e))
print(evaluate(e))

try:
  e2 = EqExpr(AddExpr(3, 5), SubExpr(11, True))
  print(e2)
  check(e2)
except Exception as err:
  print(f"error: {err}")

