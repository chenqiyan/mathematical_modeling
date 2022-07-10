Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
from scipy.optimize import linprog
 
c=np.array([-2,-3,5])
Aeq=np.array([[1,1,1])
             
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
Aeq=np.array([[1,1,1]])
             
beq=np.array([7])
             
A=np.array([[-2,5,-1],[1,3,1]])
             
b=np.array([-10,12])
             
x1,x2,x3=(0,None),(0,None),(0,None)
             
res=linprog(c,A,b,Aeq,beq,b=(x1,x2,x3))
             
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    res=linprog(c,A,b,Aeq,beq,b=(x1,x2,x3))
TypeError: linprog() got an unexpected keyword argument 'b'
res=linprog(c,A,b,Aeq,beq,bounds=(x1,x2,x3))
             
print(res)
             
     con: array([1.80714554e-09])
     fun: -14.571428565645032
 message: 'Optimization terminated successfully.'
     nit: 5
   slack: array([-2.24602559e-10,  3.85714286e+00])
  status: 0
 success: True
       x: array([6.42857143e+00, 5.71428571e-01, 2.35900788e-10])
