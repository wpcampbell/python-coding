import sys #imports the 'sys' module
import math #imports the 'math' module


# This program finds the distance between any two points on Earth
# using the spherical distance formula based on user input

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

#Welcomes the user
print("Welcome to the spherical distance calculator where you can find the distance between any two places on Earth!")
print()
#Asks the user for the names of the places to be calculated
a1=input("Enter the name of the first place.")
print("Okay, ",a1,".")
b1=input("Enter the name of the second place")
print("Okay ",b1,".")
#Asks the user for the latitude and longitude, one by one, for the first place
O1= floatcheck("Enter the latitude of the first place.")
a=math.radians(O1) #converts degrees to radians

y1= floatcheck("Enter the longitude of the first place.")
c= math.radians(y1)#converts degrees to radians

O2= floatcheck("Enter the latitude of the second place.")
b= math.radians(O2)#converts degrees to radians

y2=floatcheck("Enter the longitude of the second place.")
d= math.radians(y2)#converts degrees to radians
#calculates the angular distance between the two places given. Equation broken down into multiple variables in order to solve.

e= (c-d)
f= (math.cos(e))
g=(math.cos(a))*math.cos(b)
h=(math.sin(a))*math.sin(b)
i=(math.acos(h+g*f))
j=i*6300
# could not figure out how to make the equation work for both lat/long types (N/S and E/W)

#summarizes the results of the calculation
print("Ok, so the distance between ",a1,"and ",b1,"with coordinates of (",O1,"ºN/ºS,",y1,"ºE/ºW)","and (",O2,"ºN/ºS,",y2,"ºE/ºW), respectivly is",j,"km.")

print("")
#thanks the user
print("Thanks!")