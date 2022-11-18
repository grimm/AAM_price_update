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
  if (vendor == "tech") | (vendor == "west") | (vendor == "sb") | (vendor == "fil") | (vendor == "scs") | (vendor == "mass") | (vendor == "nitro") | (vendor == "rcs") | (vendor == "and") | (vendor == "yak") | (vendor == "mrw") | (vendor == "mrwm") | (vendor == "cbp") | (vendor == "cog") | (vendor == "cipa") | (vendor == "west") | (vendor == "pc") | (vendor == "tfp") | (vendor == "maxx") | (vendor == "rfn") | (vendor == "pull") | (vendor == "mag") | (vendor == "edge") | (vendor == "dia") | (vendor == "sup") | (vendor == "cov") | (vendor == "baja") | (vendor == "tom"):
    skiprow = 0
  elif (vendor == "mas") | (vendor == "kc") | (vendor == "fire") | (vendor == "kln") | (vendor == "truxm") | (vendor == "buy") | (vendor == "snow") | (vendor == "prime"):
    skiprow = 2
  elif (vendor == "odr") | (vendor == "wig") | (vendor == "lift") | (vendor == "ampm"):
    skiprow = 3
  elif (vendor == "kar") | (vendor == "arb") | (vendor == "myp") | (vendor == "golite") | (vendor == "aci"):
    skiprow = 4
  elif (vendor == "gorm") | (vendor == "eccot") | (vendor == "eccon") | (vendor == "bigm") | (vendor == "road"):
    skiprow = 5
  elif (vendor == "knkm") | (vendor == "btr") | (vendor == "knk"):
    skiprow = 6
  elif (vendor == "piaa") | (vendor == "tim") | (vendor == "adu"):
    skiprow = 7
  elif (vendor == "qf"):
    skiprow = 10
  elif vendor == "kso":
    skiprow = 16

  # Multisheet settings
  if vendor == "adu":
    multisheet = ["SuperBolt Fender Flare Set", "Wide Fender Flare Set", "Smooth Fender Flare Set", "OE Style Fender Flare Set", "Inner Fender Liner Set", "Grilles", "Hood Scoop", "Door Rocker Panels and Moldings", "Tailgate Appliqué", "Tailgate Spoiler", "Roof and Cab Spoiler_Winglets", "Front Bumper Guard", "Fender Vent Set", "Floor Liner Set ", "Off Road Full Kits", "Street Series Full Kits", "Cars and SUV", "Replacement Parts_Hardware"]

  if vendor == "tom":
    sheetname = "All Models"
  #   multisheet = ["Controls", "650 Series", "G2 (40) Series", "G2 (42) Series", "G2 (50) Series", "1034-1340 Original Series", "OLD 1046-1650 Original Series", "NEW 1046-1650 Original Series", "Railgate Series Old", "Railgate Series New", "Cantilever Series", "Railgate (25-30) Series", "Tuckunder Series", "TX Railgate Series", "Rail BiFold Series", "Rail High Cycle Gas Bottle Rack", "V2 Series"]

  # if vendor == "ampm":
  #   multisheet = ["PowerStep ", "BedSteps", "Bed Xtender "]

  if vendor == "kar":
    multisheet = ["Parts Prices", "Package Prices"]

  if vendor == "knk":
    multisheet = ["Jobsite", "Van", "Truck"]

  # if vendor == "mrw":
  #   multisheet = ["WHEELS", "ACCESSORIES"]

  # if vendor == "yak":
  #   multisheet = ["Part Info"]

  if vendor == "fire":
    multisheet = ["UMP Monitored ", " Not Monitored "]

  # Set sheetname or default to the first sheet
  # if vendor == "protec":
  #   sheetname = "price list"
  if vendor == "fil":
    sheetname = "Flat File"
    if vendor == "mas":
      sheetname = "FULL LIST"
      if vendor == "yak":
        sheetname = "Part Info"
        if vendor == "btr":
          sheetname = "Better Built"
          if vendor == "protec":
            sheetname = "2022"
            if vendor == "rfn":
              sheetname = "Sheet1"

  # Set CSV file read
  if vendor == "sb": csvfile = 1

  # Set a converter if needed
  converter = {}
  # if vendor == "tgp":
  #   converter = {"Part": str}

  return skiprow, sheetname, multisheet, csvfile, converter
