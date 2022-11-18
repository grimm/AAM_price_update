#
# tom.py
#
# This script holds functions for the vendor Tommy Gate
#
# Initial version - 11/02/2022 - Jason Grimes
#

from datetime import datetime
import unidecode
import pandas as pd

# Main vendor processing function
def do_tom(vendor_pandas, tech_cal):
    # Concat all sheet into one frame
    # frames = []
    # sheet = ["Controls", "650 Series", "G2 (40) Series", "G2 (42) Series", "G2 (50) Series", "1034-1340 Original Series", "OLD 1046-1650 Original Series", "NEW 1046-1650 Original Series", "Railgate Series Old", "Railgate Series New", "Cantilever Series", "Railgate (25-30) Series", "Tuckunder Series", "TX Railgate Series", "Rail BiFold Series", "Rail High Cycle Gas Bottle Rack", "V2 Series"]

    # for sheet in vendor_pandas:
    #     frames.append(vendor_pandas[sheet])

    # vendor_pandas = pd.concat(frames)
    # vendor_pandas = vendor_pandas[(vendor_pandas["Retail"] != "")]
    # vendor_pandas = vendor_pandas[(vendor_pandas["Cost"] != "")]
    # vendor_pandas = vendor_pandas[(vendor_pandas["Retail"] != "N/A")]
    # vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['MODEL'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "TOM" + x)
    
    # Test for bad SKUs
    # for index, item in enumerate(vendor_pandas["Part Number"]):
    #     bad_sku = item.lstrip("0")
    #     if item != bad_sku:
    #         print("TGP" + bad_sku + "|" + vendor_pandas["NewPart"][index])

    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["DESCRIPTION"].astype(str)
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    # print(vendor_pandas["MSRP"])
    vendor_pandas["GL"] = vendor_pandas["Dist. Price"].astype(float)

    len_pandas = len(vendor_pandas.axes[0])

    vendor_pandas["P1"] = ["P5/.7"] * len_pandas
    vendor_pandas["P2"] = ["P5/.7"] * len_pandas
    vendor_pandas["P3"] = ["P5/.8"] * len_pandas
    vendor_pandas["P4"] = ["P5/.8"] * len_pandas
    vendor_pandas["P5"] = ["GC"] * len_pandas

    # Set dimensions
    new_column = list("0" * len_pandas)
    vendor_pandas["Weight"] = new_column
    vendor_pandas["Length"] = new_column
    vendor_pandas["Height"] = new_column
    vendor_pandas["Width"] = new_column

    return vendor_pandas

