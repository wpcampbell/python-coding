import sys #imports sys module
import math #imports math module
#opens the file but exits the program if the file doesnt exist
try:
    citypop=open('CityPop.csv')
except:
    sys.exit()


#defines the class City
class City(object):
    #defines the __init__ method
    def __init__(self,Latitude,Longitude,City_name,City_label,Pop1970,Pop1975,Pop1980,Pop1985,Pop1990,Pop1995,Pop2000,Pop2005,Pop2010):
        self.city_name=City_name
        self.city_label=City_label
        self.latitude=Latitude
        self.longitude=Longitude
        self.pop1970=Pop1970
        self.pop1975=Pop1975
        self.pop1980=Pop1980
        self.pop1985=Pop1985
        self.pop1990=Pop1990
        self.pop1995=Pop1995
        self.pop2000=Pop2000
        self.pop2005=Pop2005
        self.pop2010=Pop2010
    #defines the printDistance method which finds the distance between two years for a city using the angular 
    #distance calculator
    def printDistance(self,othercity): 

        Cityone= self.city_label
        Citytwo= othercity.city_label
        latcityone= self.latitude
        latcitytwo= othercity.latitude
        longcityone= self.longitude
        longcitytwo= othercity.longitude
        #distance calculator 
        latcityone_rads=math.radians(float(latcityone)) #converts the first latitude from degrees to radians
        longcityone_rads= math.radians(float(longcityone))#converts the first longitude from degrees to radians
        latcitytwo_rads= math.radians(float(latcitytwo))#converts the second latitude from degrees to radians
        longcitytwo_rads= math.radians(float(longcitytwo))#converts the second longitude from degrees to radians
        #calculates the angular distance between the two places given. Equation broken down into multiple variables in order to solve.
        e= (longcityone_rads-longcitytwo_rads)
        f= (math.cos(e))
        g=(math.cos(latcityone_rads))*math.cos(latcitytwo_rads)
        h=(math.sin(latcityone_rads))*math.sin(latcitytwo_rads)
        i=(math.acos(h+g*f))
        j=i*6300
        print("The distance between",Cityone,"and",Citytwo, "is",j,"km. WOW!")
    #defines the PopChange method which takes a country and 2 years and finds the difference in population between the two years
    def printPopChange(self,year1,year2):
        firstyear=float(getattr(self,'pop'+year1))
        secondyear=float(getattr(self,'pop'+year2))
        print("The population change for",self.city_label,"from",year1,"to",year2,"was",secondyear-firstyear,"million.")

Cities= [] #creates the list Cities

for cityinfo in citypop: #starts a for loop, storing cityinfo as the information for each city
    citylist=(cityinfo.strip().split(",")) #processes each line of the csv by stripping it of new lines and splitting it into a list
    Cities.append(City(*citylist[1:])) #adds all instances of City to list Cities
    

#prints the instances of class City
for cityprint in Cities:
    print(cityprint.city_name)
    print(cityprint.city_label)
    print(cityprint.latitude)
    print(cityprint.longitude)
    print(cityprint.pop1970)
    print(cityprint.pop1975)
    print(cityprint.pop1980)
    print(cityprint.pop1985)
    print(cityprint.pop1990)
    print(cityprint.pop1995)
    print(cityprint.pop2000)
    print(cityprint.pop2005)
    print(cityprint.pop2010)

#insert test code here