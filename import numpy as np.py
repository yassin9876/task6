import numpy as np
A=np.array ([10, 20, 30, 40, 50])
B=np.array ([5 ,4 ,3 ,2 ,1])
addition = A + B
subtrution = A - B
mutiplication = A * B
division = A / B
mean_A =np.mean(A)
max_A =np.max(A)
min_A =np.min(A)
dot_product =np.dot(A,B)
reshape_A = A.reshape(5,1)
print(A)
print(B)
print(addition)
print(subtrution)
print(mutiplication)
print(division)
print(mean_A)
print(max_A)
print(min_A)
print(dot_product)
print(reshape_A)