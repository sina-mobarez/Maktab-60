from sympy import *
x = symbols('x')
f = x ** 2 + x
print('%.4f'%integrate(f ,(x,0,10)))