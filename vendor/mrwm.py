#
# mrwm.py
#
# This script holds functions for the vendor Custom Wheel House special manufacture file
#
# Initial version - 09/14/2021 - Jason Grimes
#

from datetime import datetime
import unidecode
import pandas as pd

# Main vendor processing function
def do_mrwm(vendor_pandas, tech_cal):
    # Concatinate both sheets for processing
    vendor_pandas = pd.concat(vendor_pandas, axis=0, ignore_index=True)

    # Only use rows for Method Race Wheels
    vendor_pandas = vendor_pandas[(vendor_pandas["BRAND"] == "Method Race Wheels") | (vendor_pandas["BRAND  "] == "Method Race Wheels")]
    vendor_pandas = vendor_pandas[(vendor_pandas[" MSRP "] != "N/A")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['PART NUMBER'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "MRW" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["DESCRIPTION"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas[r" MSRP "].replace("$", "").astype(float)
    vendor_pandas["P2"] = vendor_pandas["P1"]
    vendor_pandas["P3"] = vendor_pandas["P1"]
    vendor_pandas["P4"] = vendor_pandas["P1"]
    vendor_pandas["P5"] = vendor_pandas["P1"] * tech_cal["P5"]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["FREIGHT WEIGHT (LBS)"].replace('', '0').astype(float)
    vendor_pandas["Length"] = vendor_pandas["BOX L (IN)"].replace('', '0').astype(float)
    vendor_pandas["Width"] = vendor_pandas["BOX W (IN)"].replace('', '0').astype(float)
    vendor_pandas["Height"] = vendor_pandas["BOX H (IN)"].replace('', '0').astype(float)

    return vendor_pandas

