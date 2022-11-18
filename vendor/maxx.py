#
# maxx.py
#
# This script holds functions for the vendor Maxxima
#
# Initial version - 04/01/2022 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_maxx(vendor_pandas, tech_cal):
    # Remove in rows with no data
    vendor_pandas = vendor_pandas[(vendor_pandas["Qty. 1"] != "N/A")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Qty. 1"] != "NA")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Qty. 1"] != "D")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Qty. 1"] != "")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Part Number'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "MAXX" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Description"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P5"] = vendor_pandas["Qty. 1"].astype(float)

    vendor_pandas["P1"] = vendor_pandas["P5"] / tech_cal["P1"]
    vendor_pandas["P2"] = vendor_pandas["P5"] / tech_cal["P2"]
    vendor_pandas["P3"] = vendor_pandas["P5"] / tech_cal["P3"]
    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    return vendor_pandas

