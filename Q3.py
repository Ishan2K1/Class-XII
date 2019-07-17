n=int(input("Enter number here: "))
factor=[]
for i in range(1,n+1):
    if n%i==0:
        factor.append(i)
def factors(n):
    return factor
print(factors(n))
def isPrimeNo(n):
    if len(factor)==2:
        print("It is a prime number")
    else:
        print("It is not a prime number")
isPrimeNo(n)
if len(factor)>2:
    factor=factor[0:len(factor)-1]
def isPerfectNo(factor):
    Sum=0
    for i in factor:
        Sum+=i
    if Sum==n:
        print("It is a perfect Number")
    else:
        print("It is not a perfect Number")       
isPerfectNo(factor)
