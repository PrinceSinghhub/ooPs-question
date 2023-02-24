class main:
    def __init__(self):
        self.n=[1,2,3]
    def append(self):
        x=self.n
        n=int(input("Enter your range = "))
        for i in range(n):
            n = int(input("Enter your element = "))
            x.append(n)
        print(x)
    def delet(self):
        print(self.n)
        x=self.n
        print("enter which elemwnt are delet his index no")
        n = int(input("Enter your no = "))
        x.remove(n)
        print(x)
    def show(self):
        print("the list is = ",self.n)

pr=main()
print("our operation is \n1 append\n2 remove\n3 show")
n=int(input("Enter your command = "))
if n==1:
    pr.append()
elif n==2:
    pr.delet()
elif n==3:
    pr.show()
else:
    print("Enter a Valid command")


