#
# t3du.py
#
# This script holds functions for the vendor 3du
#
# Initial version - 10/10/2023 - Jason Grimes
#

from datetime import datetime
import unidecode

# Main vendor processing function
def do_3du(vendor_pandas, tech_cal):
    vendor_pandas = vendor_pandas[(vendor_pandas["MSRP"] != "TBD")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Retail MAP"] != "MAP REMOVED")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['UACE_Part#'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "3DU" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Description"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["Retail MAP"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)
    vendor_pandas["P4"] = vendor_pandas["Wholesale MAP"].astype(float)

    vendor_pandas["P5"] = vendor_pandas["P3"] * 0.6    # 40% discount from Jobber
    vendor_pandas["P5"] = vendor_pandas["P5"] * 0.95   # 5% additional discount
    # vendor_pandas["P5"] = vendor_pandas["P5"] * 0.98   # 2% marketing

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Box_Weight"].astype(str)
    vendor_pandas["Length"] = vendor_pandas["Box_Length"].astype(str)
    vendor_pandas["Width"] = vendor_pandas["Box_Width"].astype(str)
    vendor_pandas["Height"] = vendor_pandas["Box_Height"].astype(str)

    return vendor_pandas

