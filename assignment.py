##

from scipy.optimize import linear_sum_assignment
import numpy as np

T=np.array([[22,16,20,35,18],
           [20,12,35,40,26],
           [11,19,15,17,21],
           [25,30,21,37,40],
           [22,26,35,30,19]])

row_index,col_index=linear_sum_assignment(T)
print(row_index)#最优指派行索引
print(col_index)#列索引
print(T[row_index,col_index])#提取元素
print(T[row_index,col_index].sum())#求和

