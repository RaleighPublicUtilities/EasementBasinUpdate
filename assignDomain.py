import arcpy
from arcpy import env

#test
env.workspace = "Database Connections/RPUD_TESTDB.sde"
#trans
# env.workspace = "Database Connections/RPUD_TRANSDB.sde"

domName = "RPUD_BASIN_DOMAIN"
gdb = env.workspace

#check if domain exists
isDomain = False
desc = arcpy.Describe(gdb)
domains = desc.domains
for domain in domains:
	if domain == domName:
		isDomain = True
		print("Domain exists.")

#check if field exists
if isDomain == True:
	fcs = arcpy.ListFeatureClasses("", "", "RPUD.SewerCollectionNetwork")
	for fc in fcs:
		fields = arcpy.ListFields(fc)
		isBasin = False
		for field in fields:
			if field.name == "BASIN":
				isBasin = True
				print(field.name + " field exists in " + fc)
		if isBasin == True:
			#assign domain to field
			arcpy.AssignDomainToField_management(fc, "BASIN", domName)
			print("RPUD_BASIN_DOMAIN added to " + fc)
