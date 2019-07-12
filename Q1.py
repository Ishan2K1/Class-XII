l=[]
while True:
    m=input("Enter passwords here")
    if m!="":
        l.append(m)
    else:
        break
clower,cupper,cdigit,csymbol=0,0,0,0
for i in l:
    for j in i:
        if j.isdigit():
            cdigit+=1
        elif j.isalpha() and j.islower():
            clower+=1
        elif j.isalpha() and j.isupper():
            cupper+=1
        else:
            csymbol+=1
    print(clower,cupper,cdigit,csymbol)
    if cdigit>0 and clower>0 and cupper>0 and csymbol>0:
        print(i, "is a valid password")
    cdigit,clower,cupper,csymbol=0,0,0,0
