#
# sup.py
#
# This script holds functions for the vendor Holley brand SuperChips
#
# Initial version - 06/20/2022 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_sup(vendor_pandas, tech_cal):
    # Remove all rows that are not part of the brand
    vendor_pandas = vendor_pandas[(vendor_pandas["Brand"] == "SuperChips")]
    vendor_pandas = vendor_pandas[(vendor_pandas["SRP"] != "N/A")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Item'].astype(str).str.strip()
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "SUP" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Description"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P5"] = vendor_pandas["Your Price"].astype(float)
    vendor_pandas["P1"] = vendor_pandas["Your Price"] / tech_cal["P3"]
    vendor_pandas["P1"] = vendor_pandas["P1"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["P1"]
    vendor_pandas["P3"] = vendor_pandas["P1"]
    vendor_pandas["P4"] = vendor_pandas["P1"]
    
    return vendor_pandas
