def isvowel(i):
    f=open(i,'r')
    s=""
    while True:
        n=f.readline()
        if n:
            exceptions="aeiouAEIOU"
            m=n.split()
            for j in m:
                if j[0] in exceptions:
                    pass
                else:
                    s+=" "+j
                    p=f.tell()
                    f.seek(p,0)
            s+="\n"
        else:
            break
    return s  
i=input("Enter File Name:")
print(isvowel(i))          
