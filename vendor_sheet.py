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
	if (vendor == "tech") | (vendor == "tim") | (vendor == "aci") | (vendor == "nfa") | (vendor == "baja") | (vendor == "west") | (vendor == "sb") | (vendor == "fil") | (vendor == "scs") | (vendor == "ampm") | (vendor == "adu") | (vendor == "mass") | (vendor == "nitro") | (vendor == "rcs") | (vendor == "and") | (vendor == "yak") | (vendor == "snow") | (vendor == "mrwm") | (vendor == "cbp") | (vendor == "knk"):
	  skiprow = 0
	elif (vendor == "mas") | (vendor == "kc") | (vendor == "prime") | (vendor == "fire") | (vendor == "kln"):
	  skiprow = 2
	elif (vendor == "odr") | (vendor == "qf"):
	  skiprow = 3
	elif (vendor == "kar") | (vendor == "arb") | (vendor == "myp"):
	  skiprow = 4
	elif (vendor == "gorm") | (vendor == "eccot") | (vendor == "eccon") | (vendor == "rfn") | (vendor == "bigm") | (vendor == "road"):
	  skiprow = 5
	elif (vendor == "knkm"):
	  skiprow = 6
	elif vendor == "kso":
	  skiprow = 17

  # Multisheet settings
	if vendor == "ampm":
		multisheet = ["PowerStep ", "BedSteps", "Bed Xtender "]

	if vendor == "kar":
		multisheet = ["Parts Prices", "Package Prices"]

	if vendor == "knk":
		multisheet = ["Jobsite", "Van", "Truck"]

	if vendor == "mrw":
		multisheet = ["WHEELS", "ACCESSORIES"]

	# if vendor == "yak":
	# 	multisheet = ["Part Info"]

	if vendor == "fire":
		multisheet = ["2021 October Monitored Kits", "2021 October Not Monitored"]

	# Set sheetname or default to the first sheet
	# if vendor == "protec":
	# 	sheetname = "price list"
	if vendor == "fil":
		sheetname = "Flat File"
	if vendor == "mas":
		sheetname = "FULL LIST"
	if vendor == "yak":
		sheetname = "Part Info"

	# Set CSV file read
	if vendor == "sb": csvfile = 1

	return skiprow, sheetname, multisheet, csvfile
