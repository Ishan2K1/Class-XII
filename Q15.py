f=open("myfile.txt",'r')
string=f.read().lower()
l=string.split()
d={}
for i in l:
    if i not in d:
        d[i]=l.count(i)
print("total number of words is:" ,len(l))
print("number of different words is:",len(d))
maximum=max(d.values())
maxword=[]
for i in d:
    if d[i]==maximum:
        maxword.append(i)
print("most common words are:", maxword)
d2={}
for i in d:
    length=len(i)
    if length not in d2:
        d2[length]=[i]
    else:
        d2[length].append(i)
def find_longest_word(x):
    return d2[max(x)]
print(find_longest_word(d2))
def filter_long_words(n):
    l=[]
    for i in d2:
        if i>n:
            l.append(d2[i])
    return l
print(filter_long_words(8))
l=filter_long_words(8)
l2=[]
for i in l:
    for j in i:
        l2.append(j)
print(l2)
f.close()
f=open("newfile.txt",'w')
newlist=[]
for i in d:
    if i in l2:
        pass
    else:
        newlist.append(i)
f.write(' '.join(newlist))
f.close()
