import arcpy
from arcpy import env

#test
env.workspace = "C:/data/BasinTest.gdb"
# env.workspace = "Database Connections/RPUD_TESTDB.sde"
#trans
# env.workspace = "Database Connections/RPUD_TRANSDB.sde"

#field object
class PUField:
	def __init__(self, d_name, d_type, d_precision, d_scale, d_len, d_alias, d_is_null, d_is_required, d_domain):
		self.d_name = d_name
		self.d_type = d_type
		self.d_precision = d_precision
		self.d_scale = d_scale
		self.d_len = d_len
		self.d_alias = d_alias
		self.d_is_null = d_is_null
		self.d_is_required = d_is_required
		self.d_domain = d_domain


#add field to featureclass
def addField(fc, newField):
	fields = arcpy.ListFields(fc)

	isField = False

	for field in fields:
		if field.name == newField.d_name:
			isField = True
			print("Field name: " + field.name)

	print(isField)
	if isField <> True:
		arcpy.AddField_management(fc, newField.d_name, newField.d_type, newField.d_precision, newField.d_scale, newField.d_len, newField.d_alias, newField.d_is_null, newField.d_is_required, newField.d_domain)
		print("Field " + newField.d_name + " has been added to " + fc)
	else:
		print("Field " + newField.d_name + " already exists.")

####################################################################################################################
#create basin field with Domain RPUD_BASIN_DOMAIN
fieldBasin = PUField("BASIN", "TEXT", "", "", 30, "Drainage Basin", "NULLABLE", "NON_REQUIRED", "RPUD_BASIN_DOMAIN")

#add basin field to Easment layer
fc = "PU_Boundaries/EasementMaintenanceAreas"
addField(fc, fieldBasin)