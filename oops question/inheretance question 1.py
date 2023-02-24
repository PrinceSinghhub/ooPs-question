class model:
    def __init__(self):
        self.mi="not10"
        self.iphone="12 pro"
        self.nokia="s5"
class price(model):
    def price(self):
        print(f"the prise of {self.mi} is : ",15000)
        print(f"the prise of {self.iphone} is : ", 150000)
        print(f"the prise of {self.nokia} is : ", 10000)
a=price()
a.price()