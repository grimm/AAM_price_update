#
# qf.py
#
# This script holds functions for the vendor Quick Fist (End of the Road)
#
# Initial version - 03/31/2021 - Jason Grimes
#

from datetime import datetime
import unidecode

# Main vendor processing function
def do_qf(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    short_desc = "Description"

    # Remove parts with no price
    vendor_pandas = vendor_pandas[(vendor_pandas["Jobber"] != "") & (vendor_pandas["PART #"] != "")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['PART #'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "QF" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[short_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP"].str.replace("$", "").astype(float)
    vendor_pandas["P2"] = vendor_pandas["P1"]
    vendor_pandas["P3"] = vendor_pandas["Jobber"].str.replace("$", "").astype(float)
    vendor_pandas["P4"] = vendor_pandas["P3"]
    vendor_pandas["P5"] = vendor_pandas["WD"].str.replace("$", "").astype(float)

    # Set dimensions and status
    vendor_pandas["Dimensions"] = vendor_pandas["Dimensions"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Dimensions"] = vendor_pandas["Dimensions"].str.replace('"', "")
    vendor_pandas["Weight"] = vendor_pandas["Master Packs"].astype(float)
    vendor_pandas["Length"] = vendor_pandas["Weight"]
    vendor_pandas["Width"] = vendor_pandas["Weight"]
    vendor_pandas["Height"] = vendor_pandas["Weight"]

    for index, item in enumerate(vendor_pandas["Dimensions"]):
        length, width, height = item.split("x")
        vendor_pandas["Length"][index] = length
        vendor_pandas["Width"][index] = width
        vendor_pandas["Height"][index] = height

    return vendor_pandas

