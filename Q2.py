n=input("Enter Number Here")
def count(n):
    return len(n)
def reverse(n):
    return n[::-1]
x=input("Enter digit to check")
def hasdigit(n,x):
    if x in n:
        return True
    else:
        return False
def show(n):
    l=[i for i in n]
    f=[str(int(i)*(10**(len(n)-int(i)))) for i in l]
    s="+".join(f)
    return s
print(count(n),reverse(n),hasdigit(n,x),show(n))
