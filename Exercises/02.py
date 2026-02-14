from z3 import *
from utils import *
set_param(proof=True)


# 02.1
# Do the following two curves intersect? If yes, in which points?
#   y = x**2
#   y = 2*x + 3



# x = Real('x')
# y = Real('y')

# c1= y == x**2
# c2= y == 2*x + 3

# sol = Solver()
# sol.add(c1, c2)

# has_solution = sol.check()


# # Print the solution
# if has_solution == sat:
#     print(f"\nThe constraints are satisfiable.", end=' ')
#     print(f"Solution: \n\t{sol.model()}")
# else:
#     print(f"\nThe constraints are unsatisfiable")
#     print(f"\nProof of unsatisfiability: \n\t", end='')
#     print(sol.proof())


# 02.2
# Do the following two circumferences intersect? If yes, in which points?
#   x**2 + y**2 = 13
#   (x-5)**2 + (y-5)**2 = 5

# x = Real('x')
# y = Real('y')

# c1= x**2 + y**2 == 13
# c2= (x-5)**2 +(y-5)**2 == 5

# sol = Solver()
# sol.add(c1, c2)

# has_solution = sol.check()


# # Print the solution
# if has_solution == sat:
#     print(f"\nThe constraints are satisfiable.", end=' ')
#     print(f"Solution: \n\t{sol.model()}")
# else:
#     print(f"\nThe constraints are unsatisfiable")
#     print(f"\nProof of unsatisfiability: \n\t", end='')
#     print(sol.proof())


# 02.3
# Prove that NOT(p AND q) implies (NOT p) OR (NOT q), providing a formal proof 

# p=Bool('p')
# q=Bool('q')

# sol=Solver()

# c1= Not(And(p,q))

# c2 = Or(Not(p), Not(q))

# c3 = Or(Not(c1), c2)

# sol.add(c3)

# has_solution = sol.check()


# # Print the solution
# if has_solution == sat:
#     print(f"\nThe constraints are satisfiable.", end=' ')
#     print(f"Solution: \n\t{sol.model()}")
# else:
#     print(f"\nThe constraints are unsatisfiable")
#     print(f"\nProof of unsatisfiability: \n\t", end='')
#     print(sol.proof())

# 02.4
# Prove that NOT(p AND q) *does not* imply (NOT p) AND (NOT q), providing a concrete counterexample
# p=Bool('p')
# q=Bool('q')

# sol=Solver()

# c1= Not(And(p,q))

# c2 = And(Not(p), Not(q))

# c3 = Not(Implies(c1,c2))

# sol.add(c3)

# has_solution = sol.check()

# # Print the solution
# if has_solution == sat:
#     print(f"\nThe constraints are satisfiable.", end=' ')
#     print(f"Solution: \n\t{sol.model()}")
# else:
#     print(f"\nThe constraints are unsatisfiable")
#     print(f"\nProof of unsatisfiability: \n\t", end='')
#     print(sol.proof())

# 02.5
# Do the following two lines intersect if x is in the interval [-10, 10]? 
# If yes, in which points? If no, why?
# x = y
# 3x = y + 25
# x = Real('x')
# y = Real('y')

# c1= x == y
# c2= 3*x == y + 25
# c3= And(x>-10,x<10)

# sol = Solver()
# sol.add(c1, c2,c3)

# has_solution = sol.check()


# # Print the solution
# if has_solution == sat:
#     print(f"\nThe constraints are satisfiable.", end=' ')
#     print(f"Solution: \n\t{sol.model()}")
# else:
#     print(f"\nThe constraints are unsatisfiable")
#     print(f"\nProof of unsatisfiability: \n\t", end='')
#     print(sol.proof())

# 02.6
# Write a function that takes as input an integer n
# and finds positive integers a, b such that a**2 - b**2 = n.
# def diffOfSquares(n_input):
#   a=Int('a')
#   b=Int('b')

#   sol=Solver()

#   c=a**2 - b**2 == n_input

#   sol.add(c)

#   has_solution = sol.check()

#   if has_solution == sat:
#     model = sol.model()
#     return model[a],model[b]

# print(diffOfSquares(123))

# 02.7
# Write a function that takes as input an integer n
# and finds positive integers a, b such that a**2 + b**2 = n.
# def sumOfSquares(n_input):
#   a=Int('a')
#   b=Int('b')

#   sol=Solver()

#   c=a**2 + b**2 == n_input

#   c1 = And(a>0,b>0)
#   sol.add(c,c1)

#   if sol.check()==sat:
#     model = sol.model()
#     return model[a],model[b]
#   else:
#     print(f"\nThe constraints are unsatisfiable")
#     print(f"\nProof of unsatisfiability: \n\t", end='')
#     print(sol.proof())
#     return None

# print(sumOfSquares(123))
# print(sumOfSquares(12345))
# print(sumOfSquares(-12))

# 02.8 Find an integer greater than 90 that can be written as a sum of squares 
# a=Int('a')
# b=Int('b')
# n=Int('n')

# sol=Solver()

# c = a**2 + b**2 == n

# c1 = n>90

# sol.add(c,c1)

# if sol.check()==sat:
#   model = sol.model()
#   print(model[n])
# else:
#   print(f"\nThe constraints are unsatisfiable")
#   print(f"\nProof of unsatisfiability: \n\t", end='')
#   print(sol.proof())

# 02.9 Find the smallest integer greater than 130 that can be written as a sum of squares
# n = Int('n')
# a = Int('a')
# b = Int('b')
# s = Solver()
# s.add(a > 0, b > 0)
# s.add(n > 130)
# s.add(n == a**2 + b**2)

# has_solution = check_and_print(s)

# while check_and_print(s) == sat:
#     m = s.model()
#     s.add(n < m[n])


# 02.10
# Write a function that takes as input a positive integer n
# and checks whether n is a prime. 
# If n is not a prime, the function should print some information 
# that proves that n is not a prime.
# def isPrime(n_input):
#   if n_input < 2:
#         print(f"{n_input} is not a prime.")
#         return

#   s = Solver()

#   d = Int('d')

#   s.add(d > 1)
#   s.add(d < n_input)
#   s.add(n_input % d == 0)

#   if s.check() == sat:
#       m = s.model()
#       divisore = m[d]
#       print(f"{n_input} is not a prime because it is divisible by {divisore}.")
#   else:
#       print(f"{n_input} is a prime number.")
#       print(s.proof())
      
# isPrime(9)

# 02.11
# Write a function that takes as input two positive integers a, b,
# and checks whether a and b can be part of a Pythagorean triple.

# def arePartOfPythagorean(a_input, b_input):
#   c = Int('c')
#   s = Solver()


#   ipotesi_1 = (a_input**2 + b_input**2 == c**2)
#   ipotesi_2 = (a_input**2 + c**2 == b_input**2)
#   ipotesi_3 = (b_input**2 + c**2 == a_input**2)
  
#   s.add(a_input > 0 and b_input > 0 and c>0)
#   s.add(Or(ipotesi_1, ipotesi_2, ipotesi_3))  

#   if s.check() == sat:
#      print( s.model())
#   else:
#     print(s.check()) 

# # arePartOfPythagorean(12, 35) # expected: sat
# # arePartOfPythagorean(33, 65) # expected: sat
# # arePartOfPythagorean(89, 39) # expected: sat
# # arePartOfPythagorean(89, 139) # expected: unsat
# arePartOfPythagorean(45, 824) # expected: unsat



# 02.12 Find in how many different ways 128 can be written as a sum of squares
# n = Int('n')
# a = Int('a')
# b = Int('b')

# s2 = Solver()
# s2.add(n == a**2 + b**2)
# s2.add(n == 128)

# counter = 0
# print("\nFinding number of solutions:")
# while check_and_print(s2) == sat:
#     counter += 1
#     m = s2.model()
#     s2.add(Or(a != m[a], b != m[b]))  # exclude current solution
# print(f"\nNumber of solutions: {counter}")