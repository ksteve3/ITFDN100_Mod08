class Product(object):
    strProductName = ""
    fltProductPrice = ""

    def __init__(self, product_name="", product_price=""):
        self.strProductName = product_name
        self.fltProductPrice = product_price


objP1 = Product()
objP2 = Product(product_name = "Soap", product_price = "3.00")

print(objP1.strProductName, objP1.fltProductPrice)
print("------------")
print(objP2.strProductName, objP2.fltProductPrice)