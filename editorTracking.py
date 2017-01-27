import arcpy
from arcpy import env

#test
env.workspace = "C:/data/BasinTest.gdb"
# env.workspace = "Database Connections/RPUD_TESTDB.sde"
#trans
# env.workspace = "Database Connections/RPUD_TRANSDB.sde"

def turnOnEditorTracking(fc):
	try:
		arcpy.EnableEditorTracking_management(fc, 'CREATEDBY', 'CREATEDON', 'EDITEDBY', 'EDITEDON', 'NO_ADD_FIELDS')
		print("Editor Tracking has been turned on for " + fc)
	except:
		pass
		print("Failed turning on Editor Tracking for " + fc)
		

def turnOffEditorTracking(fc):
	try:
		arcpy.DisableEditorTracking_management(fc)
		print("Editor Tracking has been turned off for " + fc)
	except:
		pass
		print("Failed turning off Editor Tracking for " + fc)


#######################################################################
fcs = arcpy.ListFeatureClasses("", "", "SewerCollectionNetwork")
print fcs
fcs += [u'PU_Boundaries/EasementMaintenanceAreas']
print fcs

for fc in fcs:
	turnOffEditorTracking(fc)
	# turnOnEditorTracking(fc)