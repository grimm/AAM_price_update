#
# tft.py
#
# This script holds functions for the vendor Titan Fuel Tanks
#
# Initial version - 01/03/2022 - Jason Grimes
#

from datetime import datetime
import unidecode

# Main vendor processing function
def do_tft(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    short_desc = "Short Description"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Part Number'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "TFT" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[short_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["Retail MAP "].astype(float)
    vendor_pandas["P4"] = vendor_pandas["Wholesale MAP"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["WD Cost"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["P2"]

    # Set dimensions and status
    lname = "Weight (lbs)"
    vendor_pandas[lname] = vendor_pandas[lname].replace('', '0')
    vendor_pandas["Weight"] = vendor_pandas[lname].astype(float)

    vendor_pandas["Length"] = vendor_pandas["Depth (in)"].replace("", "0").astype(float)
    vendor_pandas["Width"] = vendor_pandas["Width (in)"].replace("", "0").astype(float)
    vendor_pandas["Height"] = vendor_pandas["Height (in)"].replace("", "0").astype(float)

    return vendor_pandas

