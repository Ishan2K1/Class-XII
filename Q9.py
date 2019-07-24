#Q9 INCOMPLETE
import numpy as np
n=np.random.randint(0,50,25)
print(np.reshape(n,(5,5),order='C'))
print(np.max(n),"is the max and", np.min(n)," is the min")
x=float(input("Enter Number To Find Closest To: "))
y=np.abs(n-x)
index=np.argmin(y)
print(n[index])
Max=n[1]
for i in n:
    if np.bincount(n, weights=i)>np.bincount(Max)    
