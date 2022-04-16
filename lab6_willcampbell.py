import sys #imports sys module
import scipy as S #imports the scipi module and renames it to 'S'
from osgeo import gdal #imports gdal to process the image
from osgeo import gdalconst #imports the wrapper module to open the file
gdal.UseExceptions() #enables exceptions 

#function from mod 6, lesson 5 that checks to see if the driver can be used to process the output file
def checkDriver(Driver):
    ''' Check a gdal driver for Create and CreateCopy capabilities.
        Input can be a gdal format code (string) or driver object.
        Return boolean tuple(canRead, canCreate, canCreateCopy). '''

    canRead = canCreate = canCreateCopy = False

    if type(Driver) == str:
        try:
            Driver = gdal.GetDriverByName(Driver)
        except:
            pass

    if Driver != None: canRead = True

    try:
        metadata  = Driver.GetMetadata()
        if metadata.get(gdal.DCAP_CREATE) == 'YES': canCreate = True
    except:
        pass

    try:
        if metadata.get(gdal.DCAP_CREATECOPY) == 'YES': canCreateCopy = True
    except:
        pass

    return (canRead, canCreate, canCreateCopy)

#trys to open the tif file, if it fails, the program exits
try:
    near_IR= gdal.Open('L71026029_02920000609_B40_CLIP.tif', gdalconst.GA_ReadOnly) #opens band 4 or the near IR band
    Red= gdal.Open('L71026029_02920000609_B30_CLIP.tif', gdalconst.GA_ReadOnly) #opens band 3 or the Red band
except:
    sys.exit() #exits the program

near_IR_array=near_IR.ReadAsArray().astype(float) #converts nearIR to an array and float
Red_array=Red.ReadAsArray().astype(float) #converts Red to an array and float
    
ndvi= ((near_IR_array-Red_array)/(near_IR_array+Red_array)) #calculates the ndvi
#step 1
#gets the driver from the orginal dataset and then copies it
output_driver= near_IR
driver_copy=output_driver.GetDriver()

#step 2

#sets the dimensions, number of bands and data type for the outpt
rows     = near_IR.RasterYSize
cols     = near_IR.RasterXSize
nBands   = 1
dataType = gdalconst.GDT_Float32

#checks to see if the driver can be used to create a dataset with the existing dataset and then creates it; if not, the program exits.
if checkDriver(driver_copy)[2]: 
    output_ds= driver_copy.Create('ndvi_output.tif',cols,rows,nBands,dataType)
else:
    print("Sorry, can’t copy properties of existing dataset")
    sys.exit

#step 3
#sets the geotransform of the dataset as the same as the input files
output_ds.SetGeoTransform(output_driver.GetGeoTransform()) 

#step 4
#sets the projection of the dataset as the same as the input files
output_ds.SetProjection(output_driver.GetProjection())

#step 5
#loops through each raster of the output dataset
for i in range(output_ds.RasterCount):
  band = output_ds.GetRasterBand(i+1)

band.WriteArray(ndvi) #writes the data to a numeric array
band.SetColorInterpretation(gdalconst.GCI_GrayIndex) #sets the image color to gray
output_ds= None # "closes" the wrapper module

