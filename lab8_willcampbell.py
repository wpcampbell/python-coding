import arcpy #imports the arcpy module
import os #imports the os module
import sys #imports the sys module

arcpy.env.workspace = os.path.dirname(__file__)#sets the workspace to the folder the script is in

pwrline= r'PowerLine.shp' #stores the path of the powerline shapefile
parcels= r'Parcels.shp'  #stores the path of the parcels shapefile 


try:
    cursor=arcpy.da.SearchCursor(pwrline,['SHAPE@']) #creates a cursor for the powerline shapefile
    parcel_desc= arcpy.Describe(parcels) #gets the description of the parcels shapefile
except:
    sys.exit()

#creates a geometry object from the cursor
for row in cursor: 
    geometry= row[0]

pwrline_length=geometry.getLength("PLANAR","MILES") #finds the length of the geometry object using a planar distance and converts the 
                                                    #distance from feet to miles

print("Task 1:")
print("The powerline is",pwrline_length,"miles long!") #prints the length of the powerline shapefile in miles
print("")


print("Task 2: ")
print("The field names and their types are as follows: ")
#starts a loop to look through the fields of the parcel shapefile and then prints the names and types of the fields
for parcel_fields in parcel_desc.fields:
    parcel_name= parcel_fields.name
    parcel_type= parcel_fields.type
    print(parcel_name)
    print(parcel_type)


select_parcels=arcpy.MakeFeatureLayer_management(parcels) #creates a feature layer from parcels
pwrline_crossed=arcpy.SelectLayerByLocation_management(select_parcels,"CROSSED_BY_THE_OUTLINE_OF",pwrline) #creates a feature based off the selection of parcels that are crossed by the powerline
cursor_parcels= arcpy.da.SearchCursor(select_parcels,['SITUSADDR','AREA']) #creates a cursor that searches for the addresses and areas of the parcels

#starts a loop to look through the parcels and if a parcel is crossed by the pwrline, its information is printed
print("Task 3:")
print("The addresses and areas of the parcels that are crossed by the powerline are as follows: ")
for features in cursor_parcels:
    if pwrline_crossed:
        print(features)
    
      


#task 4
#removes PwrLineBuffer.shp if it already exists 
if arcpy.Exists('PwrLineBuffer.shp'):
    arcpy.Delete_management('PwrLineBuffer.shp')

buffer_250_ft= arcpy.Buffer_analysis(pwrline,"PwrLineBuffer","250 Feet") #creates a 250 ft buffer around the powerline
selected_parcels_buffer= arcpy.SelectLayerByLocation_management(select_parcels,"WITHIN",buffer_250_ft)



if arcpy.Exists('Parcels_Buffer.shp'):
    arcpy.Delete_management('Parcels_Buffer.shp')

Parcels_Buffer=arcpy.CopyFeatures_management(selected_parcels_buffer,"Parcels_Buffer.shp")

print("")
print("Task 4:")
print("DING! Parcels_Buffer created!")
