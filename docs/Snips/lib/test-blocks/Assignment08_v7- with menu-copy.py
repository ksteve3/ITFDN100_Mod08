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
lstOfProductObjects = []  # A list of objects that acts as a 'table' of rows


class Product():
    #strProductName = ""
    #fltProductPrice = ""


    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Kstevens>,<11-30-19>,Modified code to complete assignment 8
    """

    def __init__(self, product_name, product_price):
        self.__product_name = product_name
        self.__product_price = product_price

    # product_name
    @property
    def product_name(self):  # The name must match the attribute!
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers")

    # #product_price
    @property
    def product_price(self):  # The name must match the attribute!
        return str(self.__product_price)

    @product_price.setter
    def product_price(self, value):
      self.__product_price = value

    def to_string(self):
        return self.__str__()

    def __str__(self):
        return self.product_name + ", $" + self.product_price
    #@instancemethod
    def Add(self, Value1, Value2):
        return Value1 + Value2

    # @instancemethod
    # def Add(self, objP1, objP2):
    #     return objP1 + objP2

# objP1 = Product("Apples", "1.75")
# # objP2 = Product("Pears", "1.99")
# print(objP1)
# # objP1.product_name = 'apple'
# # objP1.product_price ='$1.75'
# # print(objP1.product_name, objP1.product_price)

# #product_name
# print("Test Numbers-------------")
# try:
#     objP1.product_name = 123
# except Exception as e:
#     print(e)
# print("Test Reading Attribute -------")
# try:
#     print(objP1.__product_name)
# except Exception as e:
#     print(e.__doc__)
# print("Test Assigning Attribute -----------")
# objP1.__product_name = '123'
# print(objP1.product_name)
#
# #product_price
# print("Test Numbers-------------")
# try:
#     objP1.product_price = abc
# except Exception as e:
#     print(e)
# print("Test Reading Attribute -------")
# try:
#     print(objP1.__product_price)
# except Exception as e:
#     print(e.__doc__)
# print("Test Assigning Attribute -----------")
# objP1.__product_price = 'abc'
# print(objP1.product_price)

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #


class FileProcessor:
    """ Processing the data to and from a text file """

    @staticmethod
    def ReadFileDataToFile(file_name, list_of_rows):
        """
        Desc - Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        file = open(file_name, "r")
        for line in file:
            data = line.split(",")
            row = {"Task": data[0].strip(), "Priority": data[1].strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def WriteListDataToFile(file_name, list_of_rows):
        """
        Desc - Writes data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        # ToDo/done: Place processing code in a new function
        objFile = open(strFileName, "w")
        for dicRow in lstOfProductObjects:  # Write each row of data to the file
            objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        objFile.close()
        return list_of_rows


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ A class for perform Input and Output """

    @staticmethod
    def OutputMenuItems():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data
        2) Add a new item.
        3) Save Data to File
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def InputMenuChoice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def ShowCurrentItemsInList(list_of_rows):
        """ Shows the current items in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current items ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def GetsNewTaskandPriority():
        global strTask
        global strPriority
        # Step 3.2.a - Ask user for new task and priority
        # ToDo/done: Place IO code in a new function
        strTask = str(input("What is the product name? - ")).strip()  # Get task from user
        strPriority = str(input("What is the product price?- ")).strip()  # Get priority from user
        print()  # Add an extra line for looks

    @staticmethod
    def AddNewTaskandPriority():
        # Step 3.2.b  Add item to the List/Table
        # ToDo/done: Place processing code in a new function
        dicRow = {"Task": strTask, "Priority": strPriority}  # Create a new dictionary row
        lstOfProductObjects.append(dicRow)  # Add the new row to the list/table
        IO.ShowCurrentItemsInList(lstOfProductObjects)  # Show current data in the list/table


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Step 1 - When the program starts, Load data from products.txt.
FileProcessor.ReadFileDataToFile(strFileName, lstOfProductObjects)  # read file data

# Step 2 - Display a menu of choices to the user
while(True):
    IO.OutputMenuItems()  # Shows menu
    strChoice = IO.InputMenuChoice()  # Get menu option

    # Step 3 - Process user's menu choice
    # Step 3.1 Show current data
    if (strChoice.strip() == '1'):
        IO.ShowCurrentItemsInList(lstOfProductObjects)  # Show current data in the list/table
        continue  # to show the menu


    # Step 3.2 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):

        # ToDo/done: Place IO code in new function
        IO.GetsNewTaskandPriority() #Asks user for new task and priority

        # ToDo/done: Place processing code in a new function
        IO.AddNewTaskandPriority() #Add New Task and Priority to list
        continue  # to show the menu


    # Step 3.3 - Save tasks to the products.txt file
    elif(strChoice == '3'):

        #Step 3.3.a - Show the current items in the table
        IO.ShowCurrentItemsInList(lstOfProductObjects)  # Show current data in the list/table

        #Step 3.3.b - Ask if user if they want save that data
        if("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):  # Double-check with user

            # ToDo/done: Place processing code in a New function
            FileProcessor.WriteListDataToFile(strFileName, lstOfProductObjects) # Write each row of data to the file

            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:  # Let the user know the data was not saved
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
        continue  # to show the menu

    # Step 3.4 - Reload data from the products.txt file (clears the current data from the list/table)
    elif (strChoice == '4'):
        print("Warning: This will replace all unsaved changes. Data loss may occur!")  # Warn user of data loss
        strYesOrNo = input("Reload file data without saving? [y/n] - ")  # Double-check with user
        if (strYesOrNo.lower() == 'y'):
            lstOfProductObjects.clear()  # Added to fix bug 1.1.2030
            FileProcessor.ReadFileDataToFile(strFileName, lstOfProductObjects)  # Replace the current list data with file data
            IO.ShowCurrentItemsInList(lstOfProductObjects)  # Show current data in the list/table
        else:
            input("File data was NOT reloaded! Press the [Enter] key to return to menu.")
            IO.ShowCurrentItemsInList(lstOfProductObjects)  # Show current data in the list/table
        continue  # to show the menu

    # Step 3.5 - Exit the program
    elif (strChoice == '5'):
        break   # and Exit

# Main Body of Script  ---------------------------------------------------- #