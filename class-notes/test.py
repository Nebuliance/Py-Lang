from ast import *

# \x.x
id = AbsExpr(VarDecl("x"), IdExpr("x"))

# true = \a.\b.a 
t = AbsExpr("a", AbsExpr("b", IdExpr("a")))

# false = \a.\b.b
f = AbsExpr("a", AbsExpr("b", IdExpr("b")))

# and
land = \
  AbsExpr("p", 
    AbsExpr("q", 
      AppExpr(
        AppExpr(
          IdExpr("p"), IdExpr("q")), IdExpr("p"))))

e1 = AppExpr(AppExpr(land, t), f)

print(t)
print(f)
print(land)
print(id)
print(e1)
print(step(e1))