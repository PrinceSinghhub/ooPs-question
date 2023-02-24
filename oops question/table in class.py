class ho:
    def __init__(self, n):
        self.num = n

    def pr(self):
        for i in range(1, self.num):
            print(i * 2)

    def aj(self):
        a = 10
        b = 30
        c = a + b
        print(c)


t = ho(11)
t.pr()
t.aj()