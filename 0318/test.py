import copy
A = {1, 2, 3}
B = copy.copy(A)
A.remove(2)
print(B)