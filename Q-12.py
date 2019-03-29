f=open("q1.txt",'a')
s=" i am appending more text now"
f.write(s)
f.close()
f=open("q1.txt",'r')
l=f.readlines()
x=0
for i in l:
    x+=1
    print(str(x)+"th"+" "+i)
f.close()
length=len(l)
print(l[length-1])
f=open("q1.txt",'r')
f.seek(10,0)
print(f.readline())
n=int(input("Enter line number to be read"))
print(l[n-1])
f.close()
f=open("q1.txt",'r')
entire=f.read().upper()
allwords=entire.split()
l=[]
for i in allwords:
    l+=i[0]
l2=[]
for i in l:
    if i in l2:
        continue
    else:
        print("Words beginning with", i ,"are:", l.count(i))
        l2.append(i)
