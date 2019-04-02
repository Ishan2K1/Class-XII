f=open("students.txt",'r')
l=[]
s=""
while True:
        n=f.readline()
        if n:
            n=n.split()
            l.append(tuple(n))
        else:
            break
print(l)
for i in range(len(l)):
    l[i]=list(l[i])
for i in range(len(l)):
    l[i][1]=int(l[i][1])
for i in range(len(l)):
    for j in range(len(l)-1-i):
        if l[j][1]>l[j+1][1]:
            l[j][1],l[j+1][1]=l[j+1][1],l[j][1]
for i in l:
    i=tuple(i)
print(l)
