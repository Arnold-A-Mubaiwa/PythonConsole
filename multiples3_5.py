import numpy as np
list =[]
for i in range(1,100):
    if i%3==0 and i%5==0:
        list.append(i)
print(multiples:=np.array(list))
# or
x  = np.arange(1,100)
print(x[(x%3==0) & (x%5==0)])