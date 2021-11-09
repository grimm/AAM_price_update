#
# wes.py
#
# This script holds functions for the vendor Westin
#
# Initial version - 1/12/2021 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_wes(vendor_pandas, prod_group, tech_cal):
    # Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Set text to pull out display parts
    bad_parts = ["Display", "Sample", "Catalog", "Guide", "Brochure", "Public", "Profile", "display", "Banner"]

    # Remove displays and pricing quote rows
    vendor_pandas = vendor_pandas[(vendor_pandas["MSRP/List"] != "0.00")]
    vendor_pandas = vendor_pandas[(vendor_pandas["MSRP/List"] != "")]
    vendor_pandas = vendor_pandas[~vendor_pandas[long_desc].str.contains('|'.join(bad_parts))]
    vendor_pandas = vendor_pandas[~vendor_pandas[short_desc].str.contains('|'.join(bad_parts))]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Part Number'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "WES" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP/List"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)

    vendor_pandas["P2"] = vendor_pandas["P3"]
    for index, item in enumerate(vendor_pandas["MAP Retail"]):
        #print(index)
        if item == "":
            vendor_pandas["P2"][index] = vendor_pandas["P1"][index] * tech_cal["P2"]
        else:
            vendor_pandas["P2"][index] = item

    vendor_pandas["P4"] = vendor_pandas["P3"] * tech_cal["P4"]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight - IN POUNDS"].replace(" ", "0").replace("", "0").astype(float)
    vendor_pandas["Length"] = vendor_pandas["Length"].replace(" ", "0").replace("", "0").astype(float)
    vendor_pandas["Width"] = vendor_pandas["Weight"].replace(" ", "0").replace("", "0").astype(float)
    vendor_pandas["Height"] = vendor_pandas["Height"].replace(" ", "0").replace("", "0").astype(float)

    # Set product groups
    vendor_pandas["Group Code"] = vendor_pandas["NewPart"]
    for index, item in enumerate(vendor_pandas[short_desc]):
        vendor_pandas["Group Code"][index] = 99999
        for key, value in prod_group.items():
            if item == key:
                vendor_pandas["Group Code"][index] = value
        if vendor_pandas["Group Code"][index] == 99999:
            print(item)

    return vendor_pandas

