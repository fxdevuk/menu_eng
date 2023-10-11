# Import all modules/component
import readproducts, addproducts, updateproducts, deleteproducts, searchproducts, categorizeproducts, advices, instructions, about

# Function to read the respective menu file(s)
def menuFiles():
    with open("menu_eng/productsMenuMain.txt") as mainMenu1:
        userMainMenu = mainMenu1.read()

    with open("menu_eng/engineeringMenu.txt") as mainMenu2:
        userReportMenu = mainMenu2.read()
    
    return userMainMenu, userReportMenu # return as a tuple[str, str]
    # we can access a tupel based on index 

# userChoices = menuFiles()
# print(userChoices[0])
# print(userChoices[1])

# function for the main songs menu 
def menuEng_menu():
    options = 0 # create an option variable an initialise it with integer value 0
    optionsList = ["1","2","3","4","5","6","7","8"] # create a list with string values

    # call/invoke the menuFiles function
    userChoices = menuFiles()

    # while options(0) not in optionsList(["1","2","3","4","5","6"])
    while options not in optionsList: # this will call the menuFiles function and display the menu repeatedly
         print(userChoices[0])

         # re-assign the value of the option variable(input has a string datatype by default) 
         options = input("Enter an option: ") #1/2/3/4/5/6

        #  check  to see if the reassigned options variable is not in the list (optionsList)
         if options not in optionsList:
            print(f"{options} is not a valid choice in the menu!")
    return options
 
# call/invoke the songs_menu function
# print(songs_menu())

# function for the reports sub menu

def report_subMenu():
    options = 0
    optionsList = ["1","2","3","4"]
    reportChoices = menuFiles()

    while options not in optionsList:
        print(reportChoices[1])


        options = input("Enter an option: ") #1/2/3

        if options not in optionsList:
            print(f"{options} is not a valid choice in the reports sub menu!")
    return options


# Run the main program by calling both songs main menu and report sub menu in a while loop and if statemament

# create a boolean variable 
mainProgram = True

while mainProgram: #same as while True
    mainMenu = menuEng_menu()  # assign the songs_menu to the mainMenu variable

    # mainMenu will now hold values from the songs_menu function (1/2/3/4/5/6....)

     #check/compare if the value from the mainMenu is the same as the value in strings and call a 
     #python file and a function in the python file 
    
    if mainMenu == "1":
        instructions.read_Instructions()

    elif mainMenu == "2":
        # call/invoke a python file and a function within that file 
        readproducts.read_data()

    elif mainMenu == "3":
        addproducts.insert_data()

    elif mainMenu == "4":
        updateproducts.update_data()

    elif mainMenu == "5":
        deleteproducts.delete_data()
    
    elif mainMenu == "6":
        # reports submenu 
        reportsProgram = True # create a boolean variable

    elif mainMenu == "7":
        about.readAbout()

        while reportsProgram:
            reportSubMenu = report_subMenu()# assign the report_subMenu to the reportSubMenu variable

            # reportSubMenu will now hold values from the songs_menu function (1/2/3...)

            #check/compare if the value from the reportSubMenu is the same as the value in strings and call a 
            #python file and a function in the python file 

            if reportSubMenu == "1":
                categorizeproducts.categorize_products()
            
            elif reportSubMenu == "2":
                x = advices.readAdvices()
                print(x)

            elif reportSubMenu == "3":
                searchproducts.reportSearch()

            else:
                # re-assign the value of reportsProgram = False (to exit the program)
                reportsProgram = False
                input("Press enter to return to the main options.")


    else:
        # re-assign the value of mainProgram = False (to exit the program)
        mainProgram = False
input("Press enter to quit the Menu Engineering application.")




       





    
    
    