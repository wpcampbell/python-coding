import sys #imports the 'sys' module
# This program calculates either the area of a triangle or a trapezoid.

#This block defines the function 'floatcheck' which checks to see if an entry in the program is a float type
#If the user prints something else other than a float, an error statement prints 4 times 
#and the system exits after that.
def floatcheck(prompt):
    loopCount=0
    while loopCount<4:
        loopCount+=1
        a=input(prompt)
        try:
            print('\nyou typed an input of', a,'and its type is,',type(a))
            a = float(a)
            return(a)
        except:
            print("This is not a float. A float is a number with a floating decimal point. Please try again :)")
    print("Sorry, you have entered too many invalid responses, please try again")    
    sys.exit()    
# This block welcomes the user, prints a blank line and then asks if the user would like to know the area of a triangle or trapezoid
print("Hello there, welcome to the triangle and trapezoid area calculator!")
print()
shape = input("Would you like to know the area of a triangle or a trapezoid? :)")

#This block is executed if the user inputs "triangle", confirms the users selection as a triangle, asks for the input of a height 
# and a base, calculates the area of the triangle based on the inputs. Finally, the code tells the user what the area of the triangle 
# is that they input, inserts a blank line and tells the user to have a nice day
if shape == "triangle":
    print ("Okay, a triangle.")
    height = floatcheck("Please enter the height of the triangle: ")
    base = floatcheck("Please enter the base length of the triangle: ")
    areatri = 0.5 * height * base
    print("The area of a triangle with height", height, "and base", base, "is", areatri, ".")
    print()
    print("Thank you!!! As a recap, your triangle's area was", areatri,". Have a nice day :)")

#This block is executed if the user inputs "trapezoid, confirms the users seletion was a trapezoid, asks for the first base, second
# base and height of the trapezoid, calculates the area of the trapezoid based on the inputs. Finally, the code tells the user what
# the area of the trapezoid is that they input, inserts a blank line and tells the user to have a nice day 
elif shape == "trapezoid":
    print ("Okay, a trapezoid.")
    firstbase = floatcheck("Please enter the length of one of the bases of the trapezoid: ")
    secondbase = floatcheck("Please enter the length of the other base of the trapezoid: ")
    height = floatcheck("Please enter the height of the trapezoid: ")
    areatrap = 0.5 * (firstbase + secondbase) * height
    print ("The area of a trapezoid with bases of", firstbase, "and", secondbase, "and with a height of", height,"is", areatrap, ".")
    print ()
    print("Thank you!!! As a recap your trapezoid's area was:", areatrap,". Have a nice day :)")

#This block is executed if the user inputs something other than "triangle" or "trapezoid". The code then explodes because it does
#not know what to do
else:
    print ("Does not compute... bzzzzt harddrive overheating *boom*")

