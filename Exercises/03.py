from z3 import *
from utils import *
set_param(proof=True)


# 03.1 
# Find the smallest integer that can be written as a sum of two squares in two different ways
# n = Int('n')
# a = Int('a')
# b = Int('b')
# c = Int('c')
# d = Int('d')
# s = Solver()

# s.add(a > 0, b > 0)
# s.add(n == a**2 + b**2)
# s.add(n == c**2 + d**2)
# s.add(And(a!=c,a!=d))
# s.add(And(b!=c,b!=d))

# has_solution = check_and_print(s)


# while check_and_print(s) == sat:
#     m = s.model()
#     s.add(n < m[n])  # look for a smaller solution
# print(m[n])

# 03.2 
# Find the integer between 150 and 200 that can be written in the most different ways as a sum of two squares
# If there is more then one such integer, find the smallest one

# max_ways = -1
# best_n = -1

# for n_val in range(150, 201):
#     s = Solver()
#     x = Int('x')
#     y = Int('y')

#     s.add(x >= 0)
#     s.add(y >= x)
#     s.add(n_val == x**2 + y**2)

#     ways = 0

#     while s.check() == sat:
#         ways += 1
#         m = s.model()
#         s.add(Or(x != m[x], y != m[y]))

#     if ways > max_ways:
#         max_ways = ways
#         best_n = n_val


# print(f"The first number between 150 and 200 that can be written in the most different ways as a sum of two squares is: {best_n}")
# print(f"It can be written in {max_ways} different ways.")

# 03.3
# Find the closest point to the origin that satisfies the following constraints:
# x**2 + y**2 < 3
# y >= x**2 + 1

# s = Solver()
# x = Real('x')
# y = Real('y')

# s.add(x**2 + y**2 < 3)
# s.add(y >= x**2 + 1)



# while s.check() == sat: 
#     m=s.model() 
#     current_dist_sq = (m[x]**2 + m[y]**2)
#     s.add(x**2 + y**2 < current_dist_sq)   

# print(m)

# 03.4
# Find the closest point to the origin that satisfies the following constraints:
# x**2 + y**2 < 3
# y > x**2 + 1

# s = Solver()
# x = Real('x')
# y = Real('y')

# s.add(x**2 + y**2 < 3)
# s.add(y > x**2 + 1)



# while s.check() == sat: 
#     m=s.model() 
#     current_dist_sq = (m[x]**2 + m[y]**2)
#     s.add(x**2 + y**2 < current_dist_sq)   

# print(m)

# 03.5
# Gavina and Gavino go to San Benedetto market to buy apples, bananas, and carrots.
# They want to buy exactly 100 fruits, spending exactly 100€.
# They want to buy at least 1 apple, 1 banana, and 1 carrot.
# 1 banana costs 2€ (inflation...)
# 1 apple costs 1€
# 1 carrot costs 50c
#

# Ex 03.5.a How many apples, bananas, and carrots can they buy to satisfy the previous conditions?
s = Solver()

# Definiamo le variabili come interi positivi
a = Int('apples')
b = Int('bananas')
c = Int('carrots')

s.add(a >= 1, b >= 1, c >= 1)

s.add(a + b + c == 100)

# Note: We use cents to avoid real numbers and make the computation faster and more precise
s.add(100 * a + 200 * b + 50 * c == 10000)
print(s.check())


# Ex 03.5.b Is there more than a way to buy the fruit satisfying the previous conditions?
# Ex 03.5.d Compute how many possible combinations of apples, bananas, and carrots satisfy the initial conditions.

count = 0
while s.check() == sat:
    count += 1
    m = s.model()
    res_a = m[a]
    res_b = m[b]
    res_c = m[c]
    print(f"Solution {count}: Apples: {res_a}, Bananas: {res_b}, Carrots: {res_c}")
    
    s.add(Or(a != res_a, b != res_b, c != res_c))

if count == 0:
    print("No solution found.")




# Ex 03.5.c If they decide to buy at least 40 bananas, are they still able to satisfy the previous conditions?
s.add(b==40)
print(s.check())