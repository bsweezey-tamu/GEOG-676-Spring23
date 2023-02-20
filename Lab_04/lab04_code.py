
# Create a gdb and garage feature
import arcpy

arcpy.env.workspace = r'C:\DevSource\GEOG-676-Spring23\Lab_04\codes_env'
folder_path = r'C:\DevSource\GEOG-676-Spring23\Lab_04'
gdb_name = 'Lab04.gdb'
gdb_path = folder_path + '\\' + gdb_name
#arcpy.CreateFileGDB_management(folder_path, gdb_name)

csv_path = r"C:\DevSource\GEOG-676-Spring23\Lab_04\garages.csv"
garage_layer_name = 'Garage_Points'
garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_layer_name)

input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
garage_points = gdb_path + '\\' + garage_layer_name

# Open campus gdv, copy building feature to gdb
campus = r'C:\DevSource\GEOG-676-Spring23\Lab_04\Campus.gdb\Campus.gdb'
buildings_campus = campus + '\Structures'
buildings = gdb_path + '\\' + 'Buildings'

arcpy.Copy_management(buildings_campus, buildings)

# Re-projection
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage_points, gdb_path + '\Garage_Points_reprojected', spatial_ref)

# Buffer the garages
garageBuffered = arcpy.Buffer_analysis(gdb_path + '\Garage_Points_reprojected', gdb_path + '\Garage_Points_buffered', 150)

# Intersect our buffer with the buildings
arcpy.Intersect_analysis([garageBuffered, buildings], gdb_path + '\Garage_Building_Intersection', 'ALL')

arcpy.TableToTable_conversion(gdb_path + '\Garage_Building_Intersection.dbf', 'C:\DevSource\GEOG-676-Spring23\Lab_04', 'nearbyBuildings.csv')