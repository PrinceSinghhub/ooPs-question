class phebo:
    def __init__(self):
        print("Programe of phebonachi using class")
    def pr(self,num):
        number=num
        f=0
        s=1
        t=0
        i=0
        # while(i<number):#essi pur 10 no ki dega
        while (t<=number):#ye mujhi under no range dega value
            print(t)
            f=s
            s=t
            t=f+s
            i+=1
p=phebo()
n=int(input("Enter your no = "))
p.pr(n)


