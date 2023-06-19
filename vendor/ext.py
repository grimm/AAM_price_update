#
# ext.py
#
# This script holds functions for the vendor Extang
#
# Initial version - 10/29/2021 - Jason Grimes
#

from datetime import datetime
import unidecode

# Main vendor processing function
def do_ext(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Part Number'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "EXT" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)

    vendor_pandas["P2"] = vendor_pandas["MAP Retail"]
    for index, item in enumerate(vendor_pandas["P2"]):
        if item == "":
            vendor_pandas["P2"][index] = vendor_pandas["P5"][index] / tech_cal["P2"]
    vendor_pandas["P2"] = vendor_pandas["P2"].astype(float)
    vendor_pandas["P1"] = vendor_pandas["P2"]

    vendor_pandas["P4"] = vendor_pandas["MAP Wholesale / MSP"]
    for index, item in enumerate(vendor_pandas["P4"]):
        if item == "":
            vendor_pandas["P4"][index] = vendor_pandas["P5"][index] / tech_cal["P4"]
    vendor_pandas["P4"] = vendor_pandas["P4"].astype(float)

    # Set dimensions and status
    lname = "Weight - IN POUNDS"
    # print(vendor_pandas[lname].tolist())
    vendor_pandas["Weight"] = vendor_pandas[lname].astype(str).replace('', '0')
    # print(vendor_pandas["Weight"].tolist())
    vendor_pandas["Weight"] = vendor_pandas["Weight"].astype(float)

    vendor_pandas["Length"] = vendor_pandas["Length"].replace("", "0").astype(float)
    vendor_pandas["Width"] = vendor_pandas["Width"].replace("", "0").astype(float)
    vendor_pandas["Height"] = vendor_pandas["Height"].replace("", "0").astype(float)

    return vendor_pandas

