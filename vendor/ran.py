#
# ran.py
#
# This script holds functions for the vendor Rancho
#
# Initial version - 12/29/2023 - Jason Grimes
#

from datetime import datetime
import unidecode

# Main vendor processing function
def do_ran(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Remove parts with no pricing
    # vendor_pandas = vendor_pandas[(vendor_pandas["Jobber"] != "")]
    # vendor_pandas = vendor_pandas[(vendor_pandas["AAM Cost"] != "")]
    # vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Create new Status/NewPart columns
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "RAN" + x)
    
    # pull missing descriptions from application column
    for index, item in enumerate(vendor_pandas[long_desc]):
        if item == "":
            vendor_pandas[long_desc][index] = vendor_pandas["Application"][index]
            
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)

    # vendor_pandas["P1"] = vendor_pandas["P3"] / tech_cal["P1"]
    # vendor_pandas["P2"] = vendor_pandas["P3"]
    # vendor_pandas["P4"] = vendor_pandas["P3"] * tech_cal["P4"]

    # new calculations
    vendor_pandas["P1"] = vendor_pandas["P5"] / tech_cal["P1"]
    vendor_pandas["P2"] = vendor_pandas["P1"]
    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight - IN POUNDS"].replace("","0").astype(float)
    vendor_pandas["Length"] = vendor_pandas["Length"].replace("","0").astype(float)
    vendor_pandas["Width"] = vendor_pandas["Width"].replace("","0").astype(float)
    vendor_pandas["Height"] = vendor_pandas["Height"].replace("","0").astype(float)

    # Group codes
    vendor_pandas["Group Code"] = vendor_pandas["P1"]
    for index, item in enumerate(vendor_pandas[long_desc]):
        if item == "Cargo Management Cab Rack" or item == "Cargo Management Rear Rack":
            vendor_pandas["Group Code"][index] = 1
        else:
            vendor_pandas["Group Code"][index] = 0
    vendor_pandas["Group Code"] = vendor_pandas["Group Code"].astype(int)

    return vendor_pandas

