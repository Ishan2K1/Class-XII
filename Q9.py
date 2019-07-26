import numpy as np
n = np.random.randint(10, size=(5,5))
freq = 0
print(n)
print("Maximum value:", np.max(n),"Minimum value:", np.min(n))
for i in n:
    if np.bincount(i).argmax()>freq:
        freq = np.bincount(i).argmax()
x = int(input("Enter scalar value: "))
diff = np.abs(n - x).argmin()
closest=n.flat[diff]        
print("Most frequently occuring:", freq)
print("Closest value to scalar in array:", closest)
