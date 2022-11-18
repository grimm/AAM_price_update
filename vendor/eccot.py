#
# eccot.py
#
# This script holds functions for the vendor ECCO Titan version
#
# Initial version - 01/25/2021 - Jason Grimes
#

import unidecode

# Main vendor processing function
def do_eccot(vendor_pandas, tech_cal):
    # Process part number
    vendor_pandas["Part Number"] = vendor_pandas["Numeric Part No"].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "ECCO" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Description"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P5"] = vendor_pandas["WD "].astype(float) * tech_cal["P5"]
    vendor_pandas["P1"] = vendor_pandas["P5"] / tech_cal["P1"]
    vendor_pandas["P2"] = vendor_pandas["P5"] / tech_cal["P2"]
    vendor_pandas["P3"] = vendor_pandas["P5"] / tech_cal["P3"]
    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Ship Wt.\nLbs/mc"].replace("","0").astype(float)

    len_pandas = len(vendor_pandas.axes[0])
    vendor_pandas["Length"] = list("0" * len_pandas)
    vendor_pandas["Height"] = list("0" * len_pandas)
    vendor_pandas["Width"] = list("0" * len_pandas)

    return vendor_pandas
