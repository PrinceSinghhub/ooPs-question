class calculater:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        a=self.num1
        b=self.num2
        print("the addition is = ",a+b)
    def sub(self):
        a=self.num1
        b=self.num2
        print("the subtraction is = ",a-b)
    def multi(self):
        a=self.num1
        b=self.num2
        print("the multiplication is = ",a*b)
    def divid(self):
        a=self.num1
        b=self.num2
        print("the divid is = ",a/b)
    def mod(self):
        a=self.num1
        b=self.num2
        print("the mod is = ",a%b)
print("Enter your Command\n 1 add\n 2 sub\n 3 multiply\n 4 divid\n 5 mod")
a=int(input("enter your num 1 = "))
b=int(input("enter your num 1 = "))
pr=calculater(a,b)
x=int(input("Enter your command"))
if(x==1):
    pr.add()
elif(x==2):
    pr.sub()
elif(x==3):
    pr.multi()
elif(x==4):
    pr.divid()
elif(x==5):
    pr.mod()
else:
    print("Plese enter valid command")