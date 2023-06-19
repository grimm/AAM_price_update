#
# aac.py
#
# This script holds functions for the vendor ADVANCED ACCESSORY CONCEPTS
#
# Initial version - 05/10/2022 - Jason Grimes
# Changed to new format, they are no longer in AAM
#

from datetime import datetime
import unidecode

# Main vendor processing function
def do_aac(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    long_desc = "Description"

    # Remove blank items
    vendor_pandas = vendor_pandas[(vendor_pandas["MAP"] != "")]
    vendor_pandas = vendor_pandas[(vendor_pandas["WD "] != "")]
    vendor_pandas = vendor_pandas[(vendor_pandas["WD "] != 0)]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    vendor_pandas["Part Number"] = vendor_pandas["Part#"].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "AAC" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MAP"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["P1"]
    vendor_pandas["P3"] = vendor_pandas["P1"]
    vendor_pandas["P4"] = vendor_pandas["P1"]
    vendor_pandas["P5"] = vendor_pandas["WD "].astype(float)

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Ind Wt"].replace("", "0")
    vendor_pandas["Weight"].replace("2 Boxes", "0")
    vendor_pandas["Weight"].str.replace("oz", "").astype(float)
    vendor_pandas["Length"] = vendor_pandas["L"].replace("", "0")
    vendor_pandas["Length"].str.replace("2 Boxes", "0").astype(float)
    vendor_pandas["Width"] = vendor_pandas["W"].replace("", "0").astype(float)
    vendor_pandas["Height"] = vendor_pandas["H"].replace("", "0").astype(float)

    return vendor_pandas

