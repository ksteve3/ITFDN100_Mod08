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
print(objP1.__doc__()) # using the instance method __str__()
print("--------------------------")
print(product.get_object_count())
objP1 = Product("Pear")
print(Product.get_object_count())