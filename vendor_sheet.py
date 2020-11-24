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
	
	# Set skiprow or default to 1
	if (vendor == "tech") | (vendor == "tim") | (vendor == "yak") | (vendor == "aci") | (vendor == "nfa"):
	    skiprow = 0
	elif vendor == "adu":
	    skiprow = 2
	elif vendor == "gorm":
	    skiprow = 5
	elif vendor == "kso":
	    skiprow = 17

	# Set sheetname or default to ""
	if vendor == "protec":
		sheetname = "price list"

	return skiprow, sheetname
