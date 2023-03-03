#
# luv.py
#
# This script holds functions for the vendor Luverne Truck
#
# Initial version - 12/28/2021 - Jason Grimes
#

from datetime import datetime
import unidecode

# Main vendor processing function
def do_luv(vendor_pandas, tech_cal):
	# Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Remove blank items
    vendor_pandas = vendor_pandas[(vendor_pandas["MSRP/List"] != "")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Process part number
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["NewPart"].apply(lambda x: "LUV" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc].astype(str)
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"] + " " + vendor_pandas["Application"].astype(str)
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas['P1'] = vendor_pandas['MSRP/List'].astype(float)
    vendor_pandas["P2"] = vendor_pandas["MAP Retail"]
    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)

    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    for index, item in enumerate(vendor_pandas["P2"]):
        if item == "":
            vendor_pandas["P2"][index] = vendor_pandas["P1"][index]

    vendor_pandas["P2"] = vendor_pandas["P2"].astype(float)

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight - IN POUNDS"].replace("", "0").astype(float)
    vendor_pandas["Length"] = vendor_pandas["Length"].astype(str).replace("", "0")
    vendor_pandas["Width"] = vendor_pandas["Width"].astype(str).replace("", "0")
    vendor_pandas["Height"] = vendor_pandas["Height"].astype(str).replace("", "0")

    return vendor_pandas
