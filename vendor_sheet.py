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
	if (vendor == "tech") | (vendor == "tim") | (vendor == "yak") | (vendor == "aci") | (vendor == "nfa") | (vendor == "baja") | (vendor == "west") | (vendor == "vms") | (vendor == "sb") | (vendor == "fil"):
	  skiprow = 0
	  if vendor == "sb": csvfile = 1
	elif (vendor == "adu") | (vendor == "prime"):
	  skiprow = 2
	elif (vendor == "amp") | (vendor == "odr"):
	  skiprow = 3
	elif vendor == "kar":
	  skiprow = 4
	  multisheet = 1
	elif vendor == "mrw":
		multisheet = ["WHEELS", "ACCESSORIES"]
	elif vendor == "road":
	  skiprow = 4
	elif (vendor == "gorm") | (vendor == "eccot") | (vendor == "eccon"):
	  skiprow = 5
	elif vendor == "wes":
	  skiprow = 8
	elif vendor == "kso":
	  skiprow = 17

	# Set sheetname or default to ""
	if vendor == "protec":
		sheetname = "price list"
	if vendor == "fil":
		sheetname = "Flat File"

	return skiprow, sheetname, multisheet, csvfile
