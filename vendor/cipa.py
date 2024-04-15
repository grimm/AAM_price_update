#
# cipa.py
#
# This script holds functions for the vendor CIPA
#
# Initial version - 01/14/2022 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_cipa(vendor_pandas, tech_cal):
    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Item'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "CIPA" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Displayable Product Title"].astype(str)
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P3"] = vendor_pandas["JOBBER updated 01/01/2024"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["WD Updated 01/01/2024"].astype(float)

    vendor_pandas["P1"] = vendor_pandas["P3"] * tech_cal["P1"]
    vendor_pandas["P2"] = vendor_pandas["P3"] / tech_cal["P2"]
    vendor_pandas["P4"] = vendor_pandas["P3"] * tech_cal["P4"]

    return vendor_pandas

