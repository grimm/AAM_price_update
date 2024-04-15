#
# aac.py
#
# This script holds functions for the vendor Skyjacker Suspentions
#
# Initial version - 11/15/2023 - Jason Grimes
#

from datetime import datetime
import unidecode

# Main vendor processing function
def do_sky(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    long_desc = "DESCRIPTION"

    # Remove blank items
    vendor_pandas = vendor_pandas[(vendor_pandas["MAP"] != "")]
    # vendor_pandas = vendor_pandas[(vendor_pandas["WD "] != "")]
    # vendor_pandas = vendor_pandas[(vendor_pandas["WD "] != 0)]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # print(vendor_pandas.columns)

    vendor_pandas["Part Number"] = vendor_pandas["PART NO"].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "SKY" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MAP"]
    vendor_pandas["P2"] = vendor_pandas["P1"]
    vendor_pandas["P3"] = vendor_pandas["P1"]
    vendor_pandas["P4"] = vendor_pandas["P1"]

    vendor_pandas["P5"] = vendor_pandas["P1"].astype(float) * tech_cal["P5"]
    vendor_pandas["P5"] = vendor_pandas["P5"].astype(float)

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["WEIGHT"].replace("", "0").astype(float)
    vendor_pandas["Length"] = vendor_pandas["LENGTH"].str.replace(" ", "").replace("", "0").astype(float)
    vendor_pandas["Width"] = vendor_pandas["WIDTH"].replace("", "0").astype(float)
    vendor_pandas["Height"] = vendor_pandas["HEIGHT"].replace("", "0").astype(float)

    return vendor_pandas

