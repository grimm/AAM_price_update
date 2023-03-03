#
# cov.py
#
# This script holds functions for the vendor Covercraft
#
# Initial version - 07/11/2022 - Jason Grimes
#

from datetime import datetime
import unidecode
import yaml

# Main vendor processing function
def do_cov(vendor_pandas, tech_cal):
    # Load yaml list of current SKUs
    with open('vendor/cov_skus.yaml', encoding='utf8') as f:
        cov_skus = yaml.load(f, Loader=yaml.FullLoader)

    skus_list = list(cov_skus.keys())
    # print(skus_list)

    # Remove promotional stuff
    vendor_pandas = vendor_pandas[(vendor_pandas["Part Number"].isin(skus_list))]
    vendor_pandas = vendor_pandas.reset_index(drop=True)


    # Create new Status/NewPart columns
    vendor_pandas['NewPart'] = vendor_pandas['Part Number'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["NewPart"].apply(lambda x: "COV" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Part Description"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["New MAP"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["P1"]
    vendor_pandas["P3"] = vendor_pandas["New Jobber"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["New Cost"].astype(float)
    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Package Weight (PG)"]
    vendor_pandas["Length"] = vendor_pandas["Package Length (IN)"]
    vendor_pandas["Width"] = vendor_pandas["Package Width (IN)"]
    vendor_pandas["Height"] = vendor_pandas["Package Height (IN)"]

    return vendor_pandas

