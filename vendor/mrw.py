#
# mrw.py
#
# This script holds functions for the vendor Custom Wheel House
#
# Initial version - 02/24/2021 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv
import pandas as pd

# Main vendor processing function
def do_mrw(vendor_pandas, tech_cal):
    print(vendor_pandas["WHEELS"].axes[0])
    print(vendor_pandas["ACCESSORIES"].axes[0])
    # Concatinate both sheets for processing
    # vendor_pandas = pd.concat(vendor_pandas, axis=0)
    vendor_pandas = pd.concat(vendor_pandas, axis=0, ignore_index=True)

    # Merge badly named columns
    vendor_pandas[" MSRP "] = vendor_pandas[" MSRP "].fillna(vendor_pandas["MSRP PRICE"])
    vendor_pandas["PART NUMBER"] = vendor_pandas["PART NUMBER"].fillna(vendor_pandas[" PART NUMBER "])
    vendor_pandas["BOX L (IN)"] = vendor_pandas["BOX L (IN)"].fillna(vendor_pandas["LENGTH (IN)"])
    vendor_pandas["BOX W (IN)"] = vendor_pandas["BOX W (IN)"].fillna(vendor_pandas["WIDTH (IN)"])
    vendor_pandas["BOX H (IN)"] = vendor_pandas["BOX H (IN)"].fillna(vendor_pandas["HIEGHT (IN)"])
    vendor_pandas["FREIGHT WEIGHT (LBS)"] = vendor_pandas["FREIGHT WEIGHT (LBS)"].fillna("0")
    
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

