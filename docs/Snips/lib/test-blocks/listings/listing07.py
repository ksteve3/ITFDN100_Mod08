class Demo1:
    var1 = "Some Data"

class Demo2:
    var1 = "Some Data"
    def __str__(self):
        return self.var1 +  ", " + self.var1
d1 = Demo1()
lstOfProductObjects = [1, 2]
print(lstOfProductObjects.__str__())

d2 = Demo2()
s = str(d2)
print(s)
print(d2)
print(d2.__str__())
