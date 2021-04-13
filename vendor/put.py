#
# put.py
#
# This script holds functions for the vendor PUTCO
#
# Initial version - 05/13/2021 - Jason Grimes
#

from datetime import datetime
import unidecode

# Main vendor processing function
def do_put(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Part Number'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "PUT" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["MAP Retail"]

    for index, item in enumerate(vendor_pandas["P2"]):
        if item == "":
            vendor_pandas["P2"][index] = vendor_pandas["Unilateral Retail"][index]
            if vendor_pandas["P2"][index] == "":
                vendor_pandas["P2"][index] = vendor_pandas["P3"][index]

    vendor_pandas["P2"] = vendor_pandas["P2"].astype(float)
    vendor_pandas["P1"] = vendor_pandas["P2"]
    vendor_pandas["P4"] = vendor_pandas["P3"] * tech_cal["P4"]
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)

    # Set dimensions and status
    lname = "Weight - IN POUNDS"
    vendor_pandas[lname] = vendor_pandas[lname].replace('', '0')
    vendor_pandas[lname] = vendor_pandas[lname].replace('A', '0')
    vendor_pandas["Weight"] = vendor_pandas[lname].astype(float)

    vendor_pandas["Length"] = vendor_pandas["Length"].replace("", "0").astype(float)
    vendor_pandas["Width"] = vendor_pandas["Width"].replace("", "0").astype(float)
    vendor_pandas["Height"] = vendor_pandas["Height"].replace("", "0").astype(float)

    return vendor_pandas

