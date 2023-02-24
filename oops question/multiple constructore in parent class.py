class maa:
    def __init__(self):
        self.r1 = 100
        self.r2 = 101
        self.r3 = 102
        self.r4 = 103
        self.r5 = 104
    def __int__(self):
        self.a1=17
        self.a2 = 18
        self.a3 = 16
        self.a4 = 19
        self.a5 = 20
    def age(self):
        a=self.a1
        b=self.a2
        c=self.a3
        d=self.a4
        e=self.a5
class me(maa):
    def __init__(self):
        self.n1="khushi"
        self.n2 = "ajeet"
        self.n3 = "codex"
        self.n5 = "coder"
        self.n5 = "python"
        super().__init__()
    def excess(self):
        print(self.n1)
a=me()
a.excess()
