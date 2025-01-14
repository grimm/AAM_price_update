#
# truxm.py
#
# This script holds functions for the vendor Truxedo
#
# Initial version - 1/27/2022 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_truxm(vendor_pandas, prod_group, tech_cal):
    # Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Create new Status/NewPart columns
    vendor_pandas["Part Number"] = vendor_pandas["Part ID"]
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].astype(str).apply(lambda x: "TRUX" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Description"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP"]
    vendor_pandas["P3"] = vendor_pandas["JOBBER"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["MSP"].astype(float)

    vendor_pandas["P2"] = vendor_pandas["P3"]
    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]


    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight\n(lbs)"].astype(float)
    vendor_pandas["Length"] = vendor_pandas["Length"].astype(str).apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Length"] = vendor_pandas["Length"].astype(str).apply(lambda x: x.strip('"'))
    vendor_pandas["Length"] = vendor_pandas["Length"].astype(float)

    vendor_pandas["Height"] = vendor_pandas["Height"].astype(str).apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Height"] = vendor_pandas["Height"].astype(str).apply(lambda x: x.strip('"'))
    vendor_pandas["Height"] = vendor_pandas["Height"].astype(float)

    vendor_pandas["Width"] = vendor_pandas["Width"].astype(str).apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Width"] = vendor_pandas["Width"].astype(str).apply(lambda x: x.strip('"'))
    vendor_pandas["Width"] = vendor_pandas["Width"].astype(float)

    return vendor_pandas

