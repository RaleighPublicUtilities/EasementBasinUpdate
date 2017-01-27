import arcpy
from arcpy import env

# env.workspace = "C:/data/BasinTest.gdb"
#test
env.workspace = "Database Connections/RPUD_TESTDB.sde"
#trans
# env.workspace = "Database Connections/RPUD_TRANSDB.sde"

fcs = arcpy.ListFeatureClasses("", "", "RPUD.SewerCollectionNetwork")
domDict = {"BEAVER EAST": "BEAVER EAST", 
				"BEAVER-SW": "BEAVER-SW", 
				"BEAVERDAM-KN": "BEAVERDAM-KN",
				"BEAVERDAM-ZN": "BEAVERDAM-ZN", 
				"BEAVERDAM-ZS": "BEAVERDAM-ZS", 
				"BENSON": "BENSON", 
				"BIG BRANCH": "BIG BRANCH", 
				"BIG BRANCH SOUTH": "BIG BRANCH SOUTH", 
				"BLACK": "BLACK",
				"BUFFALO LOWER": "BUFFALO LOWER", 
				"BUFFALO UPPER": "BUFFALO UPPER", 
				"BUFFALO-G": "BUFFALO-G", 
				"BUSHY": "BUSHY", 
				"CEDAR-PERRY-LITTLE": "CEDAR-PERRY-LITTLE", 
				"CRABTREE":	"CRABTREE", 
				"CRABTREE LAKE": "CRABTREE LAKE", 
				"CRABTREE-N": "CRABTREE-N", 
				"DUTCHMAN-SWIFT": "DUTCHMAN-SWIFT", 
				"FALLS LOWER": "FALLS LOWER", 
				"FALLS UPPER": "FALLS UPPER", 
				"HALEYS-CRABTREE": "HALEYS-CRABTREE", 
				"HARE SNIPE": "HARE SNIPE", 
				"HARRIS CREEK":	"HARRIS CREEK", 
				"HORSE": "HORSE", 
				"HOUSE": "HOUSE", 
				"LITTLE BRIER":	"LITTLE BRIER", 
				"LITTLE-FOWLERS-HOMINY": "LITTLE-FOWLERS-HOMINY", 
				"LITTLE-JUNIPER-GUFFY": "LITTLE-JUNIPER-GUFFY", 
				"LITTLE-S": "LITTLE-S", 
				"LOWER BARTON":	"LOWER BARTON", 
				"LOWER SWIFT":	"LOWER SWIFT", 
				"MARKS LOWER": "MARKS LOWER", 
				"MARKS UPPER": "MARKS UPPER", 
				"MARSH": "MARSH", 
				"MIDDLE-M":	"MIDDLE-M", 
				"MIDDLE-S":	"MIDDLE-S", 
				"MINE":	"MINE", 
				"MINGO": "MINGO", 
				"MOCCASIN TRIBUTARY": "MOCCASIN TRIBUTARY", 
				"NEUSE": "NEUSE", 
				"NEUSE-P": "NEUSE-P", 
				"NEUSE-R": "NEUSE-R", 
				"NEUSE-S": "NEUSE-S", 
				"PANTHER MIDDLE": "PANTHER MIDDLE", 
				"PERRY": "PERRY", 
				"PIGEON HOUSE":	"PIGEON HOUSE", 
				"POPLAR": "POPLAR", 
				"RICHLAND":	"RICHLAND", 
				"RICHLAND-WF": "RICHLAND-WF", 
				"RICHLAND-WF-N": "RICHLAND-WF-N", 
				"ROCHESTER": "ROCHESTER", 
				"ROCKY": "ROCKY", 
				"SIMMONS": "SIMMONS", 
				"SMITH CREEK": "SMITH CREEK", 
				"SNIPES": "SNIPES", 
				"SOUTHGATE": "SOUTHGATE", 
				"SWIFT-LONG-LYNN-SPEIGHT": "SWIFT-LONG-LYNN-SPEIGHT", 
				"SYCAMORE":	"SYCAMORE", 
				"TOMS CREEK": "TOMS CREEK", 
				"TURKEY": "TURKEY", 
				"UPPER BARTON":	"UPPER BARTON", 
				"UPPER SWIFT": "UPPER SWIFT", 
				"WALNUT": "WALNUT", 
				"WALNUT-NW": "WALNUT-NW", 
				"WHITEOAK":	"WHITEOAK",
				"WILDCAT": "WILDCAT", 
				"X2": "X2", 
				"X4": "X4", 
				"X6": "X6", 
				"X7": "X7"}
basinDict = {}

for fc in fcs:
	try:
		with arcpy.da.SearchCursor(fc, 'BASIN') as cursor:
			# try:
				for row in cursor:
					if row[0] is not None:
						if row[0] not in basinDict:
							if row[0] not in domDict:
								# print(str(row[0]) + " is not a valid value!")
								raw_input(str(row[0]) + " is not a valid value! Press Enter to continue...")
							else:
								basinDict.update({row[0]: 1})
							# print(row[0])
						else:
							basinDict[row[0]] += 1
					# else:
					# 	print(row[0])
	except:
		print(fc + " does not have BASIN field.")


for key, val in basinDict.iteritems():
	print(str(key) + ", " + str(val))