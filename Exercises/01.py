from z3 import *
from utils import *

# 01.1
# Check if the following system of equations has a solution for x and y Real numbers:
#
#   x + y + 10 = 3
#   8 = y - x

# x = Real('x')
# y = Real('y')

# c1 = x + y + 10 == 3
# c2 = 8 == y - x

# sol=Solver()
# sol.add(c1, c2)

# print(sol.check())

# 01.2 
# Check if the previous system has a solution for x and y Integer numbers

# x = Int('x')
# y = Int('y')

# c1 = x + y + 10 == 3
# c2 = 8 == y - x

# sol=Solver()
# sol.add(c1, c2)

# print(sol.check())


# 01.3
# Check if the previous system of equations has a solution if we add the following inequality,
# both for the case in which x and y Real, and in the case in which they are Integers:
#
#   x > y

# x = Real('x')
# y = Real('y')

# x = Int('x')
# y = Int('y')

# c1 = x + y + 10 == 3
# c2 = 8 == y - x
# c3 = x > y

# sol=Solver()
# sol.add(c1, c2, c3)
# print(sol.check())


# 01.4
# Check if there exists Boolean values b1, b2, b3 such that:
#   (b1 OR b2) AND ((NOT b2) OR b3)

# b1= Bool('b1')
# b2= Bool('b2')
# b3= Bool('b3')

# c1= Or(b1,b2)
# c2= Or(Not(b2),b3)

# sol=Solver()
# sol.add(c1,c2)

# print(sol.check())

# 01.5
# Check if the following formula is satisfiable:
#
#       ((b AND x > 10) OR (x > 3 AND y > 4)) 
#   AND ((x + y)**2 == 20)
#   AND (NOT(b) OR y > 10)
#   
# where x and y are Real variables and b is a Boolean variable.

# b=Bool('b')
# x=Real('x')
# y=Real('y')

# c1 = Or(And(b, x>10), And(x>3, y>4))
# c2 = (x + y)**2 == 20
# c3 = Or( Not(b) , y>10)

# sol=Solver()
# sol.add(c1,c2,c3)

# sol.check()

# print_solver(sol)

# 01.6
# Same as 01.5 but switch the last occurrence of "NOT(b)" with "b"

# b=Bool('b')
# x=Real('x')
# y=Real('y')

# c1 = Or(And(b, x>10), And(x>3, y>4))
# c2 = (x + y)**2 == 20
# c3 = Or(b , y>10)

# sol=Solver()
# sol.add(c1,c2,c3)

# print(sol.check())

# 01.7
# Prove that NOT(p AND q) implies (NOT p) OR (NOT q)
# p = Bool('p')
# q = Bool('q')

# sol=Solver()

# c1= Not(And(p,q))

# c2= Or(Not(p), Not(q))

# c3 = Implies(c1, c2)




# sol.add(c3)

# print(sol.check())

# 01.8
# Prove that NOT(p AND q) *does not* imply (NOT p) AND (NOT q)

# p = Bool('p')
# q = Bool('q')

# sol=Solver()

# c1= Not(And(p,q))

# c2= And(Not(p), Not(q))

# c3 = Not(Implies(c1, c2))


# sol.add(c3)

# print(sol.check())
