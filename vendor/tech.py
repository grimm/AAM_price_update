#
# tech.py
#
# This script holds functions for the vendor tech
#
# Initial version - 9/24/2020 - Jason Grimes
#

import unidecode
import re

# Main vendor processing function
def do_tech(vendor_pandas, prod_group, tech_cal):
    # Remove promotional stuff
    # vendor_pandas = vendor_pandas.drop(vendor_pandas[(vendor_pandas['Product Group'] == "Hoodie ") & (vendor_pandas['Product Group'] == "Racing Polo") & (vendor_pandas['Product Group'] == "T-Shirt") & (vendor_pandas["Product Group"] == "Hat ")].index)
    vendor_pandas = vendor_pandas[(vendor_pandas["Product Group"] != "Hoodie ")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Product Group"] != "Racing Polo")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Product Group"] != "T-Shirt")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Product Group"] != "Hat ")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Copy Part column to NewPart column and modify to add TECH
    vendor_pandas.loc[:,"NewPart"] = vendor_pandas["Part"].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["NewPart"].apply(lambda x: "TECH" + x)
    
    # Create description 1
    # Only concat columns if the Color column has text in it
    vendor_pandas.loc[:,"Desc1"] = vendor_pandas["Product Group"]

    for index, item in enumerate(vendor_pandas["Desc1"]):
        # print(index, vendor_pandas["Color"][index])
        if vendor_pandas["Color"][index] != "NA":
            vendor_pandas["Desc1"][index] = item + "; " + vendor_pandas["Color"][index]

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Create description 2
    # Concat the Make, Model, and Year columns
    vendor_pandas["Desc2"] = vendor_pandas["Make"].astype(str) + " " + vendor_pandas["Model"].astype(str) + " " + vendor_pandas["Year"].astype(str)
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].str.replace("+", "")
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: x[:30]).str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: unidecode.unidecode(x))

    # Create price numbers
    colnames = list(vendor_pandas.columns)
    if ('MAP or Sug. Ret' in colnames):
        vendor_pandas["P1"] = vendor_pandas["MAP or Sug. Ret"]
    else:
        vendor_pandas["P1"] = vendor_pandas["MAP"]

    if ('JOB' in colnames):
        vendor_pandas["P3"] = vendor_pandas["JOB"]
    else:
        vendor_pandas["P3"] = vendor_pandas["Jobber"]

    vendor_pandas["P4"] = vendor_pandas["P3"] * tech_cal["P4"]
    vendor_pandas["P2"] = vendor_pandas["P1"]

    # Build group codes column
    vendor_pandas.loc[:,"Group"] = vendor_pandas["Product Group"]
   
    for index, item in enumerate(vendor_pandas["Product Group"]):
        vendor_pandas["Group"][index] = 99999
        for key, value in prod_group["tech"].items():
            if item == key:
                vendor_pandas["Group"][index] = value
        if vendor_pandas["Group"][index] == 99999:
            # print("******* Warning - " + item + " not found in product groups!")
            print(item)

    # Build Nelson cost from the TTK column
    vendor_pandas["NP5"] = vendor_pandas["TTK"] / 1.01

    vendor_pandas["Length"] = vendor_pandas["Length"].apply(lambda x: re.sub("\D", "", str(x)))
    vendor_pandas["Width"] = vendor_pandas["Width"].apply(lambda x: re.sub("\D", "", str(x)))
    vendor_pandas["Height"] = vendor_pandas["Height"].apply(lambda x: re.sub("\D", "", str(x)))

    return vendor_pandas

