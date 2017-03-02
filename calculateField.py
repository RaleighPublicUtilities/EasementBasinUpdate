import arcpy
from arcpy import env

# env.overwriteOutput = True

#test
env.workspace = "Database Connections/RPUD_TESTDB.sde"
# env.workspace = "C:/data/BasinTest.gdb"

# fc_basin = "PU_Boundaries/SewerBasins"

#trans
# env.workspace = "Database Connections/RPUD_TRANSDB.sde"

# fc = "RPUD.PU_Boundaries/RPUD.EasementMaintenanceAreas"
fc_basin = "RPUD.PU_Boundaries/RPUD.SewerBasins"

def calculateBasin(fc, basinLyr):
	fLyr = "lyr_" + fc
	arcpy.MakeFeatureLayer_management(fc, fLyr)
	
	rows = arcpy.SearchCursor(basinLyr)
	try:
		for row in rows:
			arcpy.SelectLayerByAttribute_management(basinLyr, "NEW_SELECTION", "\"OBJECTID\" = " + str(row.getValue("OBJECTID")))
			arcpy.SelectLayerByLocation_management(fLyr, "INTERSECT", basinLyr, "", "NEW_SELECTION")
			# print(str(row.getValue("BASINS")))
			arcpy.CalculateField_management(fLyr, "BASIN", "'{0}'".format(str(row.getValue("BASINS"))), "PYTHON_9.3", "")
			print("BASIN " + str(row.getValue("BASINS")) + " has been assigned to " + fc)
	except:
		pass
		print(fc + " does not have a BASIN field.")


def calculateLength(fc, field):
	fLyr = "lyr_" + fc
	arcpy.MakeFeatureLayer_management(fc, fLyr)
	# try:
	arcpy.CalculateField_management(fLyr, field, "!SHAPE.LEN!", "PYTHON_9.3", "")
	# except:
		# print(fc + "does not have a " + field + " field.")
#####################################################################################################################################
# 02/03/2017
#calculate basin for Easement
# fc = "RPUD.EasementMaintenanceAreas"
# arcpy.MakeFeatureLayer_management(fc_basin, "lyr_basin")
# calculateBasin(fc, "lyr_basin")
#calculate basin for sewer featureclasses
# fcs = arcpy.ListFeatureClasses("", "", "RPUD.SewerCollectionNetwork")
# for fc in fcs:
# 	basinLyr = "basin_" + fc
# 	arcpy.MakeFeatureLayer_management(fc_basin, basinLyr)
# 	calculateBasin(fc, basinLyr)

#
#calculate length for gravity main
env.workspace = "Database Connections/RPUD_TRANSDB.sde/RPUD.SewerCollectionNetwork"
fc = "RPUD.ssGravityMain"
field = "LENGTH"

calculateLength(fc, field)

