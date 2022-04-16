import ogr #imports ogr module
import gdal #imports gdal module
import gdalconst #imports gdalconst module
import sys #imports sys module
import os #imports os module
gdal.UseExceptions() #enables exeptions

pwrline= r'PowerLine.shp' #stores the path of the powerline shapefile 
parcels= r'Parcels.shp'  #stores the path of the parcels shapefile 

driver = ogr.GetDriverByName('ESRI Shapefile') #creates a driver for an ESRI Shapefile

#attempts to open the files, if they do not exist, then the program exits
try:
    dtasrce_pwrline=driver.Open(pwrline,gdalconst.GA_ReadOnly)
    dtasrce_parcels=driver.Open(parcels,gdalconst.GA_ReadOnly)
except:
    sys.exit()

# powerline information
layer_pwrline= dtasrce_pwrline.GetLayer(0) #gets the powerline layer
feature_pwrline= layer_pwrline.GetNextFeature() #gets the powerline feature
geom_pwrline= feature_pwrline.GetGeometryRef() #gets the powerline geometry

#powerline length
length_ft_pwrline= geom_pwrline.Length() #finds the length of the powerline shapefile in its default measurement unit, feet
length_miles_pwrline= length_ft_pwrline/5280 #coverts the length of the powerline shapefile in feet to miles
print("Task 1:")
print("The powerline is",length_miles_pwrline,"miles long!") #prints the length of the powerline shapefile in miles
print("")

# parcels information
layer_parcels= dtasrce_parcels.GetLayer(0) #gets the parcels layer
name_parcels= layer_parcels.GetName() #gets the name of the parcels layer
type_parcels= layer_parcels.GetGeomType() #gets the integer layer type
type_parcels_text= ogr.GeometryTypeToName(type_parcels) #converts the integer later type to text layer type
print("Task 2:")
print("The layer",name_parcels,"has a data type of",type_parcels_text,".") #prints the name and text layer type of parcels
print("")

# finding feature information in parcels
featureCount_parcels = layer_parcels.GetFeatureCount() #gets the number of features in the parcels layer


print("Task 3:")
print("The parcels' areas and addresses that cross the powerline are as follows:")
print("")
for p in range(featureCount_parcels): #starts a loop to look through all entries of the address and area attributes
    feature_parcels= layer_parcels.GetFeature(p) #finds the features of the parcels
    geom_parcels= feature_parcels.GetGeometryRef() #finds the geometry of the parcel features
    address_parcels= feature_parcels.GetField('SITUSADDR') #finds the addresses of the parcels
    area_parcels= feature_parcels.GetField('AREA') #finds the areas of the parcels
    pwrline_crosses=geom_parcels.Crosses(geom_pwrline) #creates a shape method which finds the parcels that the powerline crosses
    # prints out the addresses and areas of the parcels that the powerline crosses
    if pwrline_crosses:
        print(address_parcels)
        print(area_parcels)

print("")  
print("Task 4:")    

#step 2
#checks for another file of the same name and if it exists, it is replaced
if os.path.exists('ParcelBuffer.shp'):
    os.remove('ParcelBuffer.shp')

buffer_250_ft= geom_pwrline.Buffer(250) #creates a 250 foot buffer arond the powerline geometry

# creates a datasource for the buffer layer and exits if it cannot be created
try:
    dtasrce_buffer= driver.CreateDataSource('ParcelsBuffer.shp')
except:
    sys.exit()

#step 3
SRS = layer_parcels.GetSpatialRef() #gets the SRS of the layer_parcels layer
buffer_layer=dtasrce_buffer.CreateLayer('ParcelsBuffer',SRS,ogr.wkbPolygon) #adds the ParcelBuffers layer

#attempts to add a feature to the new layer 
for p in range(featureCount_parcels): #starts a loop to look through all parcel features to see if theyre contained by the buffer
    feature_parcels= layer_parcels.GetFeature(p) #finds the features of the parcels
    geom_parcels= feature_parcels.GetGeometryRef() #finds the geometry of the parcel features
    buffer_contains = buffer_250_ft.Contains(geom_parcels) #creates a shape method which finds the parcels that are contained by the buffer
    #checks to see if a parcel feature is contained by the buffer. If it is, its added to the layer
    if buffer_contains:
        buffer_layer.CreateFeature(feature_parcels)
        

dtasrce_buffer=None #closes the buffer datasource
dtasrce_parcels=None #closes the parcels datasource
dtasrce_pwrline=None #closes the powerline datasource
print("...")
print("File created!") 
