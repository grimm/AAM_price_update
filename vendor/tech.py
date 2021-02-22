#
# tech.py
#
# This script holds functions for the vendor tech
#
# Initial version - 9/24/2020 - Jason Grimes
#

import unidecode

# Main vendor processing function
def do_tech(vendor_pandas, prod_group, tech_cal):
    # Copy Part column to NewPart column and modify to add TECH
    vendor_pandas.loc[:,"NewPart"] = vendor_pandas["Part"]
    vendor_pandas["NewPart"] = vendor_pandas["NewPart"].apply(lambda x: "TECH" + x)
    
    # Create new description columns
    vendor_pandas.loc[:,"Desc1"] = vendor_pandas["Product Group"]
    vendor_pandas.loc[:,"Desc2"] = vendor_pandas["Product Group"]

    # Create description 1
    # Only concat columns if the Color column has text in it
    for index, item in enumerate(vendor_pandas["Desc1"]):
        if vendor_pandas["Color"][index] != "NA":
            vendor_pandas["Desc1"][index] = item + "; " + vendor_pandas["Color"][index]

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Create description 2
    # Concat the Make, Model, and Year columns
    vendor_pandas["Desc2"] = vendor_pandas["Make"].astype(str) + " " + vendor_pandas["Model"].astype(str) + " " + vendor_pandas["Year"].astype(str)
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: x[:30]).str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: unidecode.unidecode(x))

    # Create P2 and P4 by calculation
    # Calculate P4 first as P2 uses it
    vendor_pandas["P4"] = vendor_pandas[tech_cal["main"]] / tech_cal["P4"] / 1.01

    # Calculate P2
    vendor_pandas["P2"] = vendor_pandas["P4"] / tech_cal["P2"]

    # Build group codes column
    vendor_pandas.loc[:,"Group"] = vendor_pandas["Product Group"]
   
    for index, item in enumerate(vendor_pandas["Product Group"]):
        vendor_pandas["Group"][index] = 99999
        for key, value in prod_group["tech"].items():
            if item == key:
                vendor_pandas["Group"][index] = value
        if vendor_pandas["Group"][index] == 99999:
            print("******* Warning - " + item + " not found in product groups!")

    # Build Nelson cost from the TTK column
    vendor_pandas["NP5"] = vendor_pandas["TTK"] / 1.01

    return vendor_pandas

