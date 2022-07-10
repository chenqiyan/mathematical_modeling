import numpy as np
from scipy.optimize import minimize
def func(x):
    return x[0]**2+3*x[1]**2+x[0]*x[2]
#约束条件 分别为eq和ineq  eq=0 ineq>=0
def con():
    cons=({'type':'eq','fun':lambda x:x[0]+x[1]+x[2]-70},
          {'type':'ineq','fun':lambda x:-x[0]-x[1]-3*x[2]+100},
          {'type':'ineq','fun':lambda x:-2*x[1]+x[2]-15},
          {'type':'ineq','fun':lambda x:-x[0]**2-x[1]**2+400})
    
    return cons
#上下限约束

b1,b2,b3=(0,None),(0,None),(0,None)
#设置初始猜测值
x0=np.array([10,20,40])

res=minimize(func,x0,method='SLSQP',bounds=(b1,b2,b3),constraints=con())
print(res)
    

