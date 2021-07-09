# 
# vendor_sheet.py
#
# Set number of rows to skip on the excel file import
# Also set sheet name if necessary.
#

def set_excel(vendor):
	# Set default values
	skiprow = 1
	sheetname = ""
	multisheet = []
	csvfile = 0
	
	# Set skiprow or default to 1
	if (vendor == "tech") | (vendor == "tim") | (vendor == "aci") | (vendor == "nfa") | (vendor == "baja") | (vendor == "west") | (vendor == "vms") | (vendor == "sb") | (vendor == "fil") | (vendor == "scs") | (vendor == "ampm") | (vendor == "knk") | (vendor == "adu") | (vendor == "mass") | (vendor == "nitro") | (vendor == "lnd") | (vendor == "rcs") | (vendor == "and") | (vendor == "myp") | (vendor == "bap"):
	  skiprow = 0
	elif (vendor == "prime") | (vendor == "uws") | (vendor == "mas"):
	  skiprow = 2
	elif (vendor == "odr") | (vendor == "qf"):
	  skiprow = 3
	elif (vendor == "kar") | (vendor == "arb"):
	  skiprow = 4
	elif vendor == "road":
	  skiprow = 4
	elif (vendor == "gorm") | (vendor == "eccot") | (vendor == "eccon") | (vendor == "rfn") | (vendor == "bigm"):
	  skiprow = 5
	elif vendor == "knkm":
	  skiprow = 6
	elif vendor == "yak":
	  skiprow = 9
	elif vendor == "kso":
	  skiprow = 17

  # Multisheet settings
	if vendor == "ampm":
		multisheet = ["PowerStep ", "BedSteps", "Bed Xtender "]

	if vendor == "kar":
		multisheet = ["Parts Prices", "Package Prices"]

	if vendor == "knk":
		multisheet = ["JOBSITE", "VAN", "TRUCK"]

	if vendor == "mrw":
		multisheet = ["WHEELS", "ACCESSORIES"]

	# Set sheetname or default to the first sheet
	# if vendor == "protec":
	# 	sheetname = "price list"
	if vendor == "fil":
		sheetname = "Flat File"
	if vendor == "mas":
		sheetname = "FULL LIST"

	# Set CSV file read
	if vendor == "sb": csvfile = 1

	return skiprow, sheetname, multisheet, csvfile
