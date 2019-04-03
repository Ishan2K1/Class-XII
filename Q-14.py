f=open("students.txt",'r')
l=[]
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
names=[]
for i in range(len(l)):
    if int(l[i][2])<3:
        names.append(l[i][0])
d={"CSEE":0,"MME":0,"Biology":0}
for i in range(len(l)):
  for j in d:
      if l[i][3]==j:
          d[j]+=1
print(d)
print(names)
for i in range(len(l)):
    l[i]=tuple(l[i])
print(l)
