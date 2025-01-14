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
  if (vendor == "tech") | (vendor == "west") | (vendor == "sb") | (vendor == "fil") | (vendor == "mass") | (vendor == "rcs") | (vendor == "and") | (vendor == "yak") | (vendor == "cbp") | (vendor == "cog") | (vendor == "cipa") | (vendor == "pc") | (vendor == "tfp") | (vendor == "maxx") | (vendor == "rfn") | (vendor == "pull") | (vendor == "mag") | (vendor == "edge") | (vendor == "dia") | (vendor == "sup") | (vendor == "cov") | (vendor == "tom") | (vendor == "aci") | (vendor == "vms") | (vendor == "federal") | (vendor == "aac") | (vendor == "myp") | (vendor == "cmf") | (vendor == "3du") | (vendor == "sky") | (vendor == "protec") | (vendor == "knkm") | (vendor == "road") | (vendor == "anz"):

    skiprow = 0
  elif (vendor == "mas") | (vendor == "kc") | (vendor == "fire") | (vendor == "kln") | (vendor == "truxm") | (vendor == "buy") | (vendor == "snow") | (vendor == "prime") | (vendor == "knp") | (vendor =="tft") | (vendor == "wick"):
    skiprow = 2
  elif (vendor == "wig") | (vendor == "lift") | (vendor == "ampm") | (vendor == "rdl") | (vendor == "xan"):
    skiprow = 3
  elif (vendor == "kar") | (vendor == "golite") | (vendor == "arc") | (vendor == "adu"):
    skiprow = 4
  elif (vendor == "gorm") | (vendor == "ecco") | (vendor == "bigm") | (vendor == "arb") | (vendor == "tfi"):
    skiprow = 5
  elif (vendor == "btr"):
    skiprow = 6
  elif (vendor == "tim") | (vendor == "fish"):
    skiprow = 7
  elif (vendor == "knk"):
    skiprow = 8
  elif (vendor == "ult") | (vendor == "pj"):
    skiprow = 9
  elif (vendor == "qf") | (vendor == "piaa"):
    skiprow = 10
  elif (vendor == "phoe"):
    skiprow = 12
  elif (vendor == "autc"):
    skiprow = 13
  elif vendor == "kso":
    skiprow = 16

  # Multisheet settings
  # if vendor == "adu":
  #   multisheet = ["SuperBolt Fender Flare Set", "Wide Fender Flare Set", "Smooth Fender Flare Set", "OE Style Fender Flare Set", "Inner Fender Liner Set", "Grilles", "Hood Scoop", "Door Rocker Panels and Moldings", "Tailgate Appliqué", "Tailgate Spoiler", "Roof and Cab Spoiler_Winglets", "Front Bumper Guard", "Fender Vent Set", "Floor Liner Set ", "Off Road Full Kits", "Street Series Full Kits", "Cars and SUV", "Replacement Parts_Hardware"]

  if vendor == "tom":
    sheetname = "All Models"

  if vendor == "pj":
    sheetname = "Projecta"

  # if vendor == "mrw":
  #   sheetname = "WHEELS"
  #   multisheet = ["Controls", "650 Series", "G2 (40) Series", "G2 (42) Series", "G2 (50) Series", "1034-1340 Original Series", "OLD 1046-1650 Original Series", "NEW 1046-1650 Original Series", "Railgate Series Old", "Railgate Series New", "Cantilever Series", "Railgate (25-30) Series", "Tuckunder Series", "TX Railgate Series", "Rail BiFold Series", "Rail High Cycle Gas Bottle Rack", "V2 Series"]

  # if vendor == "ampm":
  #   multisheet = ["PowerStep ", "BedSteps", "Bed Xtender "]

  if vendor == "kar":
    multisheet = ["Parts Prices", "Package Prices"]

  if vendor == "knk":
    # multisheet = ["Jobsite", "Van", "Truck"]
    multisheet = ["Jobsite"]
    # multisheet = ["Van", "Truck"]

  if vendor == "mrw":
    multisheet = ["WHEELS", "ACCESSORIES"]

  if vendor == "yak":
    multisheet = ["Part Info", "Replacement Part Info"]

  if vendor == "tim":
    multisheet = ["TIMBREN SES & AORB", "SPACER KITS"]

  if vendor == "wick":
    multisheet = ["Cab Racks", "Cab Rack Acc", "XBOX Single Lid", "XBOX Dual Lid", "IBOX Box"]

  if vendor == "fish":
    multisheet = ["BLADE-ATTACHMENT", "MOUNT KITS", "MOUNT KITS 2", "ELECTRICAL", "PLOW ACCESSORIES PG. 1", "PLOW ACCESSORIES PG. 2", "CUTTING EDGES", "TAILGATE SPREADERS", "HOPPER SPREADERS & PREWET", "SPREADER ACCESSORIES", "SIDEWALKS", "Plows - HD UTV", "Plows - MD UTV", "Plows -Subcompact Tractor", "Plows - Skid Steer", "Plows - Tractor", "Skid and Tractor Plow Accs", "Pusher Plows", "Hopper Spreaders", "Tailgate Spreaders (2)", "Drop Spreaders", "Sidewalk Management", "Additional Accessories"]

  #if vendor == "fire":
  #  multisheet = ["UMP Monitored ", " Not Monitored "]

  if vendor == "west":
    multisheet = ["Truck", "Non-Truck"]

  # Set sheetname or default to the first sheet
  # if vendor == "protec":
  #   sheetname = "price list"
  if vendor == "fil":
    sheetname = "Flat File"
  if vendor == "mas":
    sheetname = "FULL LIST"
  if vendor == "prime":
    sheetname = "Complete Price Listing"
  # if vendor == "yak":
  #   sheetname = "Part Info"
  # if vendor == "btr":
  #   sheetname = "Better Built"

  if (vendor == "dia") | (vendor == "edge") | (vendor == "sup"):
    sheetname = "Active"

  # if vendor == "protec":
  #   sheetname = "2022"

  if vendor == "rfn":
    sheetname = "Sheet1"

  if vendor == "rdl":
    sheetname = "Master Load Sheet"

  # Set CSV file read
  if vendor == "sb": csvfile = 1

  # Set a converter if needed
  converter = {}
  # if vendor == "tgp":
  #   converter = {"Part": str}

  return skiprow, sheetname, multisheet, csvfile, converter
