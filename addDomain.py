import arcpy
from arcpy import env

# env.workspace = "Database Connections/RPUD_TESTDB.sde"
env.workspace = "C:/data/BasinTest.gdb"

domName = "RPUD_BASIN_DOMAIN"
gdb = env.workspace

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

isDomain = False
#check if domain exists
desc = arcpy.Describe(gdb)
domains = desc.domains
for domain in domains:
	if domain == domName:
		# isDomain = True
		print("Domain already exists.")
		arcpy.DeleteDomain_management(gdb, domain)
		print("Domain has been deleted.")

if isDomain <> True:
	#create domain
	arcpy.CreateDomain_management(gdb, domName, domName, "TEXT", "CODED")
	print("Domain " + domName + " has been created")

	

	#add coded value to domain
	for code in domDict:
		arcpy.AddCodedValueToDomain_management(gdb, domName, code, domDict[code])
		print(code + ", " + domDict[code])
else:
	print("Domain already exists.")