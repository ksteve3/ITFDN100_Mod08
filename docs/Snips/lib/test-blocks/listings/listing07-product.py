class Product:
 # --Fields--
 # This is one of few the times a field is used as a global variable
    __counter = 0
 # -- Constructor --
    def __init__(self, product_name):
    # -- Attributes --
        self.__product_name = product_name
    # call the private method each time an object is made
        Product.__set_object_count()
# -- Properties --
# First Name
    @property # DON'T USE NAME for this directive!
    def product_name(self): # (getter or accessor)
        return str(self.__product_name).title() # Title case
    @product_name.setter # The NAME MUST MATCH the property's!
    def product_name(self, value): # (setter or mutator)
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers")

# -- Methods --
    def __str__(self):
        return self.product_name

    @staticmethod # You do not use the "self' keyword
    def get_object_count(): # This is a PUBLIC static method
        return Product.__counter

    @staticmethod # You do not use the "self" keyword
    def __set_object_count(): # This is a PRIVATE and static method
        Product.__counter += 1
# --End of class--
# --- Use the class ----

objP1 = Product("Apple")
print(objP1) # using the instance method __str__()
print(objP1.__str__()) # using the instance method __str__()
print("--------------------------")
print(Product.get_object_count())
objP1 = Product("Pear")
print(Product.get_object_count())