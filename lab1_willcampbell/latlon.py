#This program takes input of a latitude and longitude and then tells where it is on the Earth.
import sys #imports the 'sys' module

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
#Has the user input a latitude and then prints a statement based on what the user inputs. 
x=floatcheck("Please input the latitude of a location: ")
if x == 0:
    print("That location is on the equator.")
elif x >= 0 or x <= 90:
    print("That location is north of the equator.")
elif x >= -90 or x <= 0:
    print("That location is south of the equator.")
elif x > 90 or x < -90:
    print("That location does not have a valid latitude!")

#Has the user input a longitude and then prints a statement based on what the user inputs.
y=floatcheck("Please input the longitude of a location.")
if y == 0:
    print("That location is on the prime meridian.")
elif y >= 0 or y <= 180:
    print("That location is east of the prime meridian.")
elif y >=-180 or y <= 0:
    print("That location is west of the prime meridian")
elif y >180 or y < -180:
    print("That location does not have a valid longitude!")

print("Thanks!")