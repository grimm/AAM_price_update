#
# pj.py
#
# This script holds functions for the vendor Vision X USA Projecta line
#
# Initial version - 10/20/2023 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_pj(vendor_pandas, tech_cal):
    # print(vendor_pandas.columns)
    # Remove in rows with no data
    # vendor_pandas = vendor_pandas[(vendor_pandas["PartNo"] != 0)]
    # vendor_pandas = vendor_pandas.reset_index(drop=True)

  	# Put really long header text in some vars
    long_desc = "DESCRIPTION"

    # Process part number
    vendor_pandas["Part Number"] = vendor_pandas["ITEM #"].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"]
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc].astype(str)
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["JOBBER"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["P1"]
    vendor_pandas["P3"] = vendor_pandas["P1"]
    # vendor_pandas["P1"] = vendor_pandas["P3"] * tech_cal["P1"]
    vendor_pandas["P5"] = vendor_pandas["P1"] * 0.5525
    vendor_pandas["P4"] = vendor_pandas["P1"] * tech_cal["P4"]

    # Set dimensions and status
    # len_pandas = len(vendor_pandas.axes[0])
    # new_column = list("0" * len_pandas)

    # vendor_pandas["Weight"] = new_column
    # vendor_pandas["Length"] = new_column
    # vendor_pandas["Width"] = new_column
    # vendor_pandas["Height"] = new_column

    # vendor_pandas["Weight"] = vendor_pandas["T-Product Weight"].replace("", "0").astype(float)
    
    # vendor_pandas["Length"] = vendor_pandas["T-Product Length"].astype(str).replace("", "0")
    # vendor_pandas["Length"] = vendor_pandas["Length"].replace('"','')

    # vendor_pandas["Width"] = vendor_pandas["T-Product Width"].astype(str).replace("", "0")
    # vendor_pandas["Width"] = vendor_pandas["Width"].str.replace('"', '')

    # vendor_pandas["Height"] = vendor_pandas["T-Product Height"].astype(str).replace("", "0")
    # vendor_pandas["Height"] = vendor_pandas["Height"].str.replace('"','')

    return vendor_pandas
