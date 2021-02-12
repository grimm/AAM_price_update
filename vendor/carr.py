#
# carr.py
#
# This script holds functions for the vendor CARR
#
# Initial version - 02/12/2021 - Jason Grimes
#

from datetime import datetime
import csv
import unidecode

# Main vendor processing function
def do_carr(vendor_pandas, tech_cal):
	# Put really long header text in some vars
    long_desc = "Description"
    short_desc = "DESCRIPTION 2"

    # Process part number
    vendor_pandas["Part Number"] = vendor_pandas[" Part No."].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "CARR" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P3"] = vendor_pandas["Jobber/MAP"].astype(float)
    vendor_pandas["P2"] = (vendor_pandas["P3"] / tech_cal["P2"]).astype(float)
    vendor_pandas["P1"] = vendor_pandas["P2"]
    vendor_pandas["P4"] = vendor_pandas["P3"] * tech_cal["P4"]
    vendor_pandas["P5"] = vendor_pandas["P3"] * tech_cal["P5"]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["WEIGHT"].astype(float)
    vendor_pandas["Length"] = vendor_pandas["LENGTH"].astype(float)
    vendor_pandas["Width"] = vendor_pandas["WIDTH"].astype(float)
    vendor_pandas["Height"] = vendor_pandas["HEIGHT"].astype(float)

    return vendor_pandas
