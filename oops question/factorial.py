class factorial:
    def __init__(self):
        print("Programe of factorial using class")
    def pr(self,num):
        number=num
        r=1
        for i in range(1,number+1):
           r=r*i
        print("the factorial is = ",r)
p=factorial()
n=int(input("Enter your no = "))
p.pr(n)