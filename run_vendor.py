# Run vendor processing and build columns
def vendor(vendor_pandas, vendor_cal, product_groups, vendor_name, vendor):
	titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4", "P5",
                     "Length", "Width", "Height", "Weight", "Status"]
	nelson_columns = titan_columns

	if vendor_name == "aci":
	    new_pandas = vendor.do_aci(vendor_pandas, product_groups["aci"], vendor_cal["aci"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3",
	                     "P4", "P5", "Length", "Width", "Height", "Weight", "Group"]

	if vendor_name == "adu":
	    new_pandas = vendor.do_adu(vendor_pandas, vendor_cal["adu"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "ard":
	    new_pandas = vendor.do_ard(vendor_pandas, vendor_cal["ard"])

	if vendor_name == "bkr":
	    new_pandas = vendor.do_bkr(vendor_pandas, vendor_cal["bkr"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "tech":
	    new_pandas = vendor.do_tech(vendor_pandas, product_groups, vendor_cal["tech"])
	    #                 new_part   part     descriptions     P1     P2      P3      P4    P5
	    titan_columns = ["NewPart", "Part", "Desc1", "Desc2", "MAP", "P2", "Jobber", "P4", "TTK",
	                     "Length", "Width", "Height", "Weight", "Group"]
	    nelson_columns =["NewPart", "Part", "Desc1", "Desc2", "MAP", "P2", "Jobber", "P4", "NP5",
	                     "Length", "Width", "Height", "Weight", "Group"]

	if vendor_name == "tim":
	    new_pandas = vendor.do_tim(vendor_pandas, vendor_cal["tim"])
	    #                 new_part   part     descriptions       P1     P2      P3      P4    P5
	    titan_columns = ["NewPart", "PART #", "Desc1", "Desc2", "US $      List", "P2", "US $ JOBBER", "P4", "US $           J - 31%", "BOX (L)      (inches)", "BOX (D)  (inches)", "BOX(H) (inches)", "Shipping Weight (Lbs.)"]
	    nelson_columns = ["NewPart", "PART #", "Desc1", "Desc2", "US $      List", "P2", "US $ JOBBER", "P4", "US $           J - 31%", "BOX (L)      (inches)", "BOX (D)  (inches)", "BOX(H) (inches)", "Shipping Weight (Lbs.)"]

	if vendor_name == "curt":
	    new_pandas = vendor.do_curt(vendor_pandas, vendor_cal["curt"])

	if vendor_name == "fia":
	    new_pandas = vendor.do_fia(vendor_pandas, vendor_cal["fia"])

	if vendor_name == "gor":
	    new_pandas = vendor.do_gor(vendor_pandas, vendor_cal["gor"])

	if vendor_name == "gorm":
	    new_pandas = vendor.do_gorm(vendor_pandas, vendor_cal["gorm"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "knk":
	    new_pandas = vendor.do_knk(vendor_pandas, vendor_cal["knk"])

	if vendor_name == "knn":
	    new_pandas = vendor.do_knn(vendor_pandas, vendor_cal["knn"])

	if vendor_name == "nfa":
	    new_pandas = vendor.do_nfa(vendor_pandas, vendor_cal["nfa"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "piaa":
	    new_pandas = vendor.do_piaa(vendor_pandas, product_groups["piaa"], vendor_cal["piaa"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3",
	                     "P4", "P5", "Length", "Width", "Height", "Weight", "Group"]

	if vendor_name == "protec":
	    new_pandas = vendor.do_protec(vendor_pandas, vendor_cal["protec"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "warn":
	    new_pandas = vendor.do_warn(vendor_pandas, product_groups["warn"], vendor_cal["warn"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight", "Group"]
	    nelson_columns = titan_columns

	if vendor_name == "rsp":
	    new_pandas = vendor.do_rsp(vendor_pandas, vendor_cal["rsp"])

	if vendor_name == "kso":
	    new_pandas = vendor.do_kso(vendor_pandas, vendor_cal["kso"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "par":
	    new_pandas = vendor.do_par(vendor_pandas, vendor_cal["par"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "rig":
	    new_pandas = vendor.do_rig(vendor_pandas, vendor_cal["rig"])

	if vendor_name == "yak":
	    new_pandas = vendor.do_yak(vendor_pandas, vendor_cal["yak"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	return new_pandas, titan_columns, nelson_columns
