#This program converts either a latitude or longitude between DD and DMS formats

#functions 

#converts an input of dms to dd
def dmstodd (degminsec):
    degrees,minutes,seconds = degminsec
    
    if degrees < 0: #if the input is negative dms, the input goes here
       a = degrees - (minutes/60) - (seconds/3600)
       return(a)
    else: #if the input is postitive dms, the input goes here
        a = degrees + (minutes/60) + (seconds/3600)
        return(a)

#converts an input of dd to dms
def ddtodms (decimaldegrees):
    decdeg=decimaldegrees

    if decdeg < 0:#if the input is negative dd, the input goes here
        degrees= int(decdeg)
        decpart= -(decdeg-degrees)

        decpart2= decpart * 60
        minutes=(int(decpart2))

        decpart3=decpart2-minutes
        seconds= (int(decpart3 * 60))
        return degrees,minutes,seconds
    else:#if the input is postitive dd, the input goes here
        degrees= int(decdeg)
        decpart= (decdeg-degrees)

        decpart2= decpart * 60
        minutes=(int(decpart2))

        decpart3=decpart2-minutes
        seconds= (int(decpart3 * 60))
        return degrees,minutes,seconds

# now for the main program

print("Hello! Welcome to the coordinate converter!") #welcomes the user
print("") #prints blank space
userinput=input("Please enter a latitude or longitude in the either the (degrees,minutes,seconds) or decimal degrees format: ") #input statement


#tests to see if the input is dms
if "," in userinput:
    dmssplit=userinput.split(',')
    splitzero=float(dmssplit[0])
    splitone=float(dmssplit[1])
    splittwo=float(dmssplit[2])
    tupledms=(splitzero,splitone,splittwo)
    dd=dmstodd(tupledms)
    print("Your input is in the form of degrees,minutes and seconds.")
    print("The degrees,minutes and seconds you entered converts to",dd,"in decimal degrees.")
#If the input is not dms, the program defaults to decimal degrees and goes here
else:
    ddfloat=float(userinput)
    dms=ddtodms(ddfloat)
    print("Your input is in the form of decimal degrees.")
    print("The decimal degrees you entered converts to",dms[0], "degrees", dms[1],"minutes,and",dms[2],"seconds.")
#error trap could be placed here if ddfloat or dmssplit used elif and the else statement told the user they theyve made an incorrect input, told them their input type and 
#gave them more chances to put in the correct input