import arcpy

# assign bands
source = r"C:\DevSource\GEOG-676-Spring23\Lab_07"
band1 = arcpy.sa.Raster(source + r"\band01.tif") #blue
band2 = arcpy.sa.Raster(source + r"\band02.tif") #green
band3 = arcpy.sa.Raster(source + r"\band03.tif") #red
band4 = arcpy.sa.Raster(source + r"\band04.tif") #NIR
combined = arcpy.CompositeBands_management([band1, band2, band3, band4], source + r"\output_combined.tif")

# hillshade
#azimuth = 315
#altitude = 45
#shadows = 'NO_SHADOWS'
#z_factor = 1
#arcpy.HillShade_3d(source + r"\DEM.tif", source + r"\output_Hillshade.tif", azimuth, altitude, shadows, z_factor)

# slope
#output_measurement = "DEGREE"
#z_factor = 1
#arcpy.Slope_3d(source + r"\DEM.tif", source + r"\output_Slope.tif", output_measurement, z_factor)

print("success!")