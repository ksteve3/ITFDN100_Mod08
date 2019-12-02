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

