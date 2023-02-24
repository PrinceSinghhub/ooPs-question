class aor:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def pr(self):
        n1=self.num1
        n2=self.num2
        print("the area of rectange is = ",n1*n2)
a=int(input("enter your num 1 = "))
b=int(input("enter your num 1 = "))
pr=aor(a,b)
pr.pr()