#
# ven.py
#
# This script holds functions for the vendor Auto Ventshade
#
# Initial version - 04/26/2021 - Jason Grimes
#

from datetime import datetime
import unidecode

# Main vendor processing function
def do_ven(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Remove rows with no price
    # vendor_pandas = vendor_pandas[(vendor_pandas["MSRP/List"] != "")]
    vendor_pandas = vendor_pandas[(vendor_pandas["AAM Cost"] != "emailed for Cost")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)
    
    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Part Number'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "VEN" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP/List"]
    vendor_pandas["P2"] = vendor_pandas["MAP Retail"]
    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)

    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    for index, item in enumerate(vendor_pandas["P1"]):
        # print("***"+item+"***")
        if item == "":
            vendor_pandas["P1"][index] = vendor_pandas["P2"][index]
        if vendor_pandas["P2"][index] == "":
            vendor_pandas["P1"][index] = vendor_pandas["P5"][index] / tech_cal["P2"]

    vendor_pandas["P1"] = vendor_pandas["P1"].astype(float)

    for index, item in enumerate(vendor_pandas["P2"]):
        # print(item)
        if item == "":
            vendor_pandas["P2"][index] = vendor_pandas["P5"][index] / tech_cal["P2"]
    vendor_pandas["P2"] = vendor_pandas["P2"].astype(float)
    
    # Set dimensions and status
    lname = "Weight - IN POUNDS"
    vendor_pandas[lname] = vendor_pandas[lname].replace('', '0')
    vendor_pandas["Weight"] = vendor_pandas[lname].astype(float)

    vendor_pandas["Length"] = vendor_pandas["Length"].replace("", "0").astype(float)
    vendor_pandas["Width"] = vendor_pandas["Width"].replace("", "0").astype(float)
    vendor_pandas["Height"] = vendor_pandas["Height"].replace("", "0").astype(float)

    return vendor_pandas

