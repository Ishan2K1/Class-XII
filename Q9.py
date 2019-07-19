#Q9 INCOMPLETE
import numpy as np
n=np.random.random((5,5))
Max,Min=0,n[1][1]
for j in n:
    for i in j:
        if i>Max:
            Max=i
        if i<Min:
            Min=i
print(n,Max,Min)
x=float(input("Enter Number To Find Closest To: "))
diff=0
num=n[1][1]
for i in n:
    for j in i:
        diff=x-i
        if diff<(x-num):
            num=i
print(num)
