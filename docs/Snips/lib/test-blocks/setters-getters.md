
## Setters-and-Getters.txt

```
# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes
#
# Module08 Course Video (https://www.youtube.com/watch?v=ZnTabY0Z-XE&feature=youtu.be), Timestamp:21:00
# _Mod8PythonProgrammingNotes.pdf (https://canvas.uw.edu/courses/1342958/files/59922398?module_item_id=9989526), Listing 1 & 2
# Starting Assignment 08 Video (https://www.youtube.com/watch?v=Zmgsg6HPxSM&feature=youtu.be)
# Assignment08.pdf (https://canvas.uw.edu/courses/1342958/modules/items/9989527)
# Assigment08-Starter.py (https://canvas.uw.edu/courses/1342958/modules/items/9996796)
#
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Kstevens,<11-30-19>,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# ITFDN100_Mod08

Getting and setters / Accessors and Mutator

```
## Directive  / @name_of_method.setter


@product_price.setter #(Setter or Mutator)
def product_price(self, value):

    if not str(value).isnumeric():
        self.__product_price = value
    else:
        raise Exception


## Directive  / @product_name.setter

@product_name.setter #(Setter or Mutator)
def product_name(self, value):

    if str(value).isnumeric() == False:
        self.__product_name = value
    else:
        raise Exception("Names cannot be numbers") #validation to make sure the data clean




## Property Directive / @property /  timestamp 33:00

@property  # (Getter or Accessors)  ## getter does not read files. Typically the
# "getter does formatting processes
def product_name(self): #The name must match the attribute!
    return str(self.__product_name).title()  # change letter casing to opposite of the name value
    # examples used to create copies of the classes.



NOTES:
# Using setters and getters as a pair or using standalone (Timestamp:44:00)


#  if you want your script to function as "write only" do pair with a "getter" directive as you
# will not get anything

# if you want your script to function as read only, leave off the "setter"
# - but doing it this way will not tallow you to change it
```

