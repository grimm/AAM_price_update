#
# mba.py
#
# This script holds functions for the vendor MOB Armor
#
# Initial version - 07/20/2021 - Jason Grimes
#

from datetime import datetime
import unidecode

# Main vendor processing function
def do_mba(vendor_pandas, tech_cal):
    # Remove in rows with no data
    # vendor_pandas = vendor_pandas[(vendor_pandas["Jobber"] != "")]
    # vendor_pandas = vendor_pandas[(vendor_pandas["Jobber"] != "0.00")]
    # vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Create new Status/NewPart columns
    # vendor_pandas['Part Number'] = vendor_pandas['Part Number'].astype(str)
    vendor_pandas['Part Number'] = vendor_pandas['SKU'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "MBA" + x)
    
    # Create new description columns
    # vendor_pandas["Desc1"] = vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Product Name"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    # vendor_pandas["P1"] = vendor_pandas["MSRP/List"].astype(float)
    vendor_pandas["P1"] = vendor_pandas["MSRP"].astype(float)
    # vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["Reseller/Jobber Price"].astype(float)
    # vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["Ditributor \"A\" Pricing"].astype(float)
    # vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)
    # vendor_pandas["P2"] = vendor_pandas["MAP Retail"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["Retail MAP"].astype(float)
    
    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    # Set dimensions and status
    # lname = "Weight - IN POUNDS"
    lname = "Packaged Weight (oz.)"

    vendor_pandas["Weight"] = vendor_pandas[lname].astype(float)
    # vendor_pandas["Length"] = vendor_pandas["Length"].astype(str)
    # vendor_pandas["Width"] = vendor_pandas["Width"].astype(str)
    # vendor_pandas["Height"] = vendor_pandas["Height"].astype(str)
    vendor_pandas["Length"] = vendor_pandas["Packaged Length (in)"].astype(str)
    vendor_pandas["Width"] = vendor_pandas["Packaged Width (in)"].astype(str)
    vendor_pandas["Height"] = vendor_pandas["Packaged Height (in)"].astype(str)

    return vendor_pandas

