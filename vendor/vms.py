#
# vms.py
#
# This script holds functions for the vendor Vision X USA
#
# Initial version - 02/01/2021 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_vms(vendor_pandas, tech_cal):
	# Put really long header text in some vars
    long_desc = "Transaction Description"

    # Process part number
    vendor_pandas["Part Number"] = vendor_pandas["Item #"].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "VMS" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc].astype(str)
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas['P1']=(vendor_pandas['Calculated MSRP'].replace( '[\$,)]','', regex=True )).astype(float)
    vendor_pandas["P2"] = vendor_pandas["Jobber"].replace( '[\$,)]','', regex=True ).astype(float)
    vendor_pandas["P3"] = vendor_pandas["P2"].astype(float)
    vendor_pandas["P4"] = vendor_pandas["P3"] * tech_cal["P4"]
    vendor_pandas["P5"] = vendor_pandas["Titan Cost"].replace( '[\$,)]','', regex=True ).astype(float)

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["T-Product Weight"].replace("", "0").astype(float)
    
    vendor_pandas["Length"] = vendor_pandas["T-Product Length"].astype(str).replace("", "0")
    vendor_pandas["Length"] = vendor_pandas["Length"].replace('"','')

    vendor_pandas["Width"] = vendor_pandas["T-Product Width"].astype(str).replace("", "0")
    vendor_pandas["Width"] = vendor_pandas["Width"].str.replace('"', '')

    vendor_pandas["Height"] = vendor_pandas["T-Product Height"].astype(str).replace("", "0")
    vendor_pandas["Height"] = vendor_pandas["Height"].str.replace('"','')

    return vendor_pandas
