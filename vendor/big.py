#
# big.py
#
# This script holds functions for the vendor Big Country
#
# Initial version - 01/27/2021 - Jason Grimes
#

from datetime import datetime
import unidecode

# Main vendor processing function
def do_big(vendor_pandas, prod_group, tech_cal):
    # Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Remove parts with no price
    vendor_pandas = vendor_pandas[(vendor_pandas["AAM Cost"] != "")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Part Number'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "BIG" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc2"] = vendor_pandas[long_desc]
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: x[30:60])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP/List"]
    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)

    vendor_pandas["P2"] = vendor_pandas["P3"]
    for index, item in enumerate(vendor_pandas["Unilateral Retail"]):
        if item == "":
            vendor_pandas["P2"][index] = vendor_pandas["P3"][index]
        else:
            vendor_pandas["P2"][index] = item

    for index, item in enumerate(vendor_pandas["P1"]):
        if item == "":
            vendor_pandas["P1"][index] = vendor_pandas["P2"][index]
    vendor_pandas["P1"] = vendor_pandas["P1"].astype(float)

    vendor_pandas["P4"] = vendor_pandas["P3"]
    for index, item in enumerate(vendor_pandas["Unilateral Wholesale"]):
        if item == "":
            vendor_pandas["P4"][index] = vendor_pandas["P3"][index] * tech_cal["P4"]
        else:
            vendor_pandas["P4"][index] = item

    # Set dimensions and status
    lname = "Weight - IN POUNDS"
    vendor_pandas[lname] = vendor_pandas[lname].astype(str)
    vendor_pandas[lname] = vendor_pandas[lname].str.replace('TBD', '0')
    vendor_pandas["Weight"] = vendor_pandas[lname].astype(float)

    vendor_pandas["Length"] = vendor_pandas[lname].astype(str)
    vendor_pandas["Length"] = vendor_pandas["Length"].str.replace('TBD', '0')
    vendor_pandas["Length"] = vendor_pandas["Length"].astype(float)

    vendor_pandas["Width"] = vendor_pandas[lname].astype(str)
    vendor_pandas["Width"] = vendor_pandas["Width"].str.replace('TBD', '0')
    vendor_pandas["Width"] = vendor_pandas["Width"].astype(float)

    vendor_pandas["Height"] = vendor_pandas[lname].astype(str)
    vendor_pandas["Height"] = vendor_pandas["Height"].str.replace('TBD', '0')
    vendor_pandas["Height"] = vendor_pandas["Height"].astype(float)

    # Set product groups
    vendor_pandas["Group"] = vendor_pandas["NewPart"]
    for index, item in enumerate(vendor_pandas[short_desc]):
        vendor_pandas["Group"][index] = 99999
        for key, value in prod_group.items():
            if item == key:
                vendor_pandas["Group"][index] = value
        if vendor_pandas["Group"][index] == 99999:
            print(item)

    return vendor_pandas

