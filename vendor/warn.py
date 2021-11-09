#
# warn.py
#
# This script holds functions for the vendor Warn Industries
#
# Initial version - 10/19/2020 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_warn(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Part Number'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "WARN" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: x[30:60])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP/List"]
    vendor_pandas["P3"] = vendor_pandas["Jobber"]
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"]

    vendor_pandas["Group Code"] = vendor_pandas["NewPart"]
    vendor_pandas["P2"] = vendor_pandas["AAM Cost"]
    for index, item in enumerate(vendor_pandas["Unilateral Retail"]):
        #print(index)
        if item == "":
            vendor_pandas["P2"][index] = vendor_pandas["P3"][index] / tech_cal["P2"]
            vendor_pandas["Group Code"][index] = 1
        else:
            vendor_pandas["P2"][index] = item
            vendor_pandas["Group Code"][index] = 0

    vendor_pandas["P4"] = vendor_pandas["AAM Cost"]
    for index, item in enumerate(vendor_pandas["Unilateral Wholesale"]):
        if item == "":
            vendor_pandas["P4"][index] = vendor_pandas["P3"][index] * tech_cal["P4"]
        else:
            vendor_pandas["P4"][index] = item

    # len_pandas = len(vendor_pandas.axes[0])
    # new_column = list("A" * len_pandas)
    # vendor_pandas["Status"] = new_column

    # Set dimensions and status
    lname = "Weight - IN POUNDS"
    vendor_pandas[lname] = vendor_pandas[lname].astype(str)
    vendor_pandas[lname] = vendor_pandas[lname].replace(' ', '0')
    vendor_pandas["Weight"] = vendor_pandas[lname].replace('', '0').astype(float)

    #print(vendor_pandas["Length"].to_list())
    vendor_pandas["Length"] = vendor_pandas["Length"].replace(' ', '0')
    vendor_pandas["Length"] = vendor_pandas["Length"].replace('', '0').astype(float)

    vendor_pandas["Width"] = vendor_pandas["Width"].replace(' ', '0')
    vendor_pandas["Width"] = vendor_pandas["Width"].replace('', '0').astype(float)

    vendor_pandas["Height"] = vendor_pandas["Height"].replace(' ', '0')
    vendor_pandas["Height"] = vendor_pandas["Height"].replace('', '0').astype(float)

    return vendor_pandas

