class ringTower:
    def __init__(self):
        self.list=[]
    def push(self,x):
        if len(self.list)==0:
            self.list.append(x)
        elif x<=self.list[0]:
            self.list.insert(0,x)
        elif x>=self.list[len(self.list)-1]:
            self.list.append(x)
    def pop(self):
        if len(self.list)==0:
            print("No Numbers in the stack!")
        else:
            self.list=self.list[1:len(self.list)-1]
ring=ringTower()        
while True:
    x=input("Enter Number Here")
    if x=="":
        print("Done!")
        break
    else:
        ring.push(int(x))
        print(ring.list)
