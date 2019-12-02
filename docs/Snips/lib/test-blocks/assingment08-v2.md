```
# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes
#
# Module08 Course Video (https://www.youtube.com/watch?v=ZnTabY0Z-XE&feature=youtu.be),
# Timestamp:21:00
# _Mod8PythonProgrammingNotes.pdf (https://canvas.uw.edu/courses/1342958/files/59922398?
# module_item_id=9989526), Listing 1 & 2
# Starting Assignment 08 Video (https://www.youtube.com/watch?v=Zmgsg6HPxSM&feature=youtu.be)
# Assignment08.pdf (https://canvas.uw.edu/courses/1342958/modules/items/9989527)
# Assigment08-Starter.py (https://canvas.uw.edu/courses/1342958/modules/items/9996796)
#
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# KStevens ,11-30-19,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #
#-------------------------Class_____________________________________________#

# Declare variables and constants
strFileName = "products.txt"  # The name of the data file
objFile = None   # An object that represents a file
strProductName = "product_name"  # A row of text data from the file
fltProductPrice = "product_price"  # A row of text data from the file
lstOfProductObjects = []  # A list of objects that acts as a 'table' of rows


class Product(object):
    strProductName = ""
    fltProductPrice = ""

    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Kstevens>,<11-30-19>,Modified code to complete assignment 8
    """

    def __init__(self, product_name="", product_price=""):
        self.__ProductName = product_name
        self.__ProductPrice = product_price

objP1 = Product()
objP2 = Product(product_name = "Apples", product_price = "$1.75")

print(objP1.strProductName, objP1.fltProductPrice)
print("------------")
print(objP2.strProductName, objP2.fltProductPrice)


# Processing  ------------------------------------------------------------- #

class FileProcessor:
    """ Processing the data to and from a text file"""

@property
def __product_name(self): #The name must match the attribute!
     return str(self.__product_name).title()


@__product_name.setter
def __product_name(self, value):
     if str(value).isnumeric() == False:
         self.__product_name = value
     else:
         raise Exception("Names cannot be numbers")

 #---------Processing  -------------------------------------------------------------

 #--------Presentation (Input/Output)  --------------------------------------------
```
