#
# snow.py
#
# This script holds functions for the vendor SnowDogg (Buyers).
#
# Initial version - 08/31/2021 - Jason Grimes
#

from datetime import datetime
import unidecode
import pandas as pd

# Main vendor processing function
def do_snow(vendor_pandas, tech_cal):
    # Create new Status/NewPart columns
    vendor_pandas = vendor_pandas[(vendor_pandas["Amount01"] != "")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    part1 = vendor_pandas[(vendor_pandas["ItemPartNumber"].str[:2] == "14")]
    part2 = vendor_pandas[(vendor_pandas["ItemPartNumber"].str[:2] == "16")]
    part3 = vendor_pandas[(vendor_pandas["ItemPartNumber"].str[:3] == "PRO")]
    part4 = vendor_pandas[(vendor_pandas["ItemPartNumber"].str[:3] == "TGS")]
    part5 = vendor_pandas[(vendor_pandas["ItemPartNumber"].str[:4] == "SHPE")]
    part6 = vendor_pandas[(vendor_pandas["ItemPartNumber"] == "3011864")]
    part7 = vendor_pandas[(vendor_pandas["ItemPartNumber"] == "3016233")]

    vendor_pandas = pd.concat([part1, part2, part3, part4, part5, part6, part7])
    
    vendor_pandas['Part Number'] = vendor_pandas['ItemPartNumber']
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "SNOW" + x)
     
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Description"].str.replace("\?", "")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: x[30:60])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["ListPrice"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["Amount01"].astype(float)

    vendor_pandas["P2"] = vendor_pandas["P5"] / tech_cal["P2"]
    vendor_pandas["P3"] = vendor_pandas["P5"] / tech_cal["P3"]
    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    # Set dimensions
    vendor_pandas["Weight"] = vendor_pandas["Weight (lbs)"].replace('', '0').astype(float)

    len_pandas = len(vendor_pandas.axes[0])
    new_column = list("0" * len_pandas)

    vendor_pandas["Length"] = new_column
    vendor_pandas["Height"] = new_column
    vendor_pandas["Width"] = new_column

    return vendor_pandas

