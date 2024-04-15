#
# knp.py
#
# This script holds functions for the vendor Knapheide
#
# Initial version - 08/10/2023 - Jason Grimes
#

from datetime import datetime
import unidecode

# Main vendor processing function
def do_knp(vendor_pandas, tech_cal):
    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['New Part Number'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "KNP" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Application"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    return vendor_pandas

