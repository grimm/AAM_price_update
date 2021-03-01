# Run vendor processing and build columns
def vendor(vendor_pandas, vendor_cal, product_groups, vendor_name, vendor):
	titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4", "P5",
                     "Length", "Width", "Height", "Weight", "Status"]
	nelson_columns = titan_columns
	titan_columns_group = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
	                       "P5", "Length", "Width", "Height", "Weight", "Group Code"]

	if vendor_name == "aci":
	    new_pandas = vendor.do_aci(vendor_pandas, product_groups["aci"], vendor_cal["aci"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3",
	                     "P4", "P5", "Length", "Width", "Height", "Weight", "Group"]

	if vendor_name == "adu":
	    new_pandas = vendor.do_adu(vendor_pandas, vendor_cal["adu"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "amp":
	    new_pandas = vendor.do_ard(vendor_pandas, vendor_cal["ard"])

	if vendor_name == "ard":
	    new_pandas = vendor.do_ard(vendor_pandas, vendor_cal["ard"])

	if vendor_name == "baja":
	    new_pandas = vendor.do_baja(vendor_pandas, vendor_cal["baja"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "big":
	    new_pandas = vendor.do_big(vendor_pandas, product_groups["big"], vendor_cal["big"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3",
	                     "P4", "P5", "Length", "Width", "Height", "Weight", "Group"]
	    nelson_columns = titan_columns

	if vendor_name == "bkr":
	    new_pandas = vendor.do_bkr(vendor_pandas, vendor_cal["bkr"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "bush":
	    new_pandas = vendor.do_bush(vendor_pandas, vendor_cal["bush"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "buy":
	    new_pandas = vendor.do_buy(vendor_pandas, vendor_cal["buy"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "tech":
	    new_pandas = vendor.do_tech(vendor_pandas, product_groups, vendor_cal["tech"])
	    #                 new_part   part     descriptions     P1     P2      P3      P4    P5
	    titan_columns = ["NewPart", "Part", "Desc1", "Desc2", "MAP or Sug. Ret", "P2", "JOB", "P4", "TTK",
	                     "Length", "Width", "Height", "Weight", "Group"]
	    nelson_columns =["NewPart", "Part", "Desc1", "Desc2", "MAP or Sug. Ret", "P2", "JOB", "P4", "NP5",
	                     "Length", "Width", "Height", "Weight", "Group"]

	if vendor_name == "tim":
	    new_pandas = vendor.do_tim(vendor_pandas, vendor_cal["tim"])
	    #                 new_part   part     descriptions       P1     P2      P3      P4    P5
	    titan_columns = ["NewPart", "PART #", "Desc1", "Desc2", "US $      List", "P2", "US $ JOBBER", "P4", "US $           J - 31%", "BOX (L)      (inches)", "BOX (D)  (inches)", "BOX(H) (inches)", "Shipping Weight (Lbs.)"]
	    nelson_columns = ["NewPart", "PART #", "Desc1", "Desc2", "US $      List", "P2", "US $ JOBBER", "P4", "US $           J - 31%", "BOX (L)      (inches)", "BOX (D)  (inches)", "BOX(H) (inches)", "Shipping Weight (Lbs.)"]

	if vendor_name == "carr":
	    new_pandas = vendor.do_carr(vendor_pandas, vendor_cal["carr"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "curt":
	    new_pandas = vendor.do_curt(vendor_pandas, vendor_cal["curt"])

	if vendor_name == "deck":
	    new_pandas = vendor.do_deck(vendor_pandas, vendor_cal["deck"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "eccon":
	    new_pandas = vendor.do_eccon(vendor_pandas, vendor_cal["eccon"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "eccot":
	    new_pandas = vendor.do_eccot(vendor_pandas, vendor_cal["eccot"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "fia":
	    new_pandas = vendor.do_fia(vendor_pandas, vendor_cal["fia"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "fil":
	    new_pandas = vendor.do_fil(vendor_pandas, vendor_cal["fil"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "gor":
	    new_pandas = vendor.do_gor(vendor_pandas, vendor_cal["gor"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "gorm":
	    new_pandas = vendor.do_gorm(vendor_pandas, vendor_cal["gorm"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "kar":
	    new_pandas = vendor.do_kar(vendor_pandas, vendor_cal["kar"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns
	    
	if vendor_name == "knk":
	    new_pandas = vendor.do_knk(vendor_pandas, vendor_cal["knk"])

	if vendor_name == "knn":
	    new_pandas = vendor.do_knn(vendor_pandas, vendor_cal["knn"])

	if vendor_name == "mrw":
	    new_pandas = vendor.do_mrw(vendor_pandas, vendor_cal["mrw"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "nfa":
	    new_pandas = vendor.do_nfa(vendor_pandas, vendor_cal["nfa"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "odr":
	    new_pandas = vendor.do_odr(vendor_pandas, vendor_cal["odr"])
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
                     "P5"]
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

	if vendor_name == "prime":
	    new_pandas = vendor.do_prime(vendor_pandas, vendor_cal["prime"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "rch":
	    new_pandas = vendor.do_rch(vendor_pandas, vendor_cal["rch"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "rig":
	    new_pandas = vendor.do_rig(vendor_pandas, vendor_cal["rig"])

	if vendor_name == "road":
	    new_pandas = vendor.do_road(vendor_pandas, vendor_cal["road"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "rug":
	    new_pandas = vendor.do_rug(vendor_pandas, vendor_cal["rug"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "rrk":
	    new_pandas = vendor.do_rrk(vendor_pandas, vendor_cal["rrk"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "sb":
	    new_pandas = vendor.do_sb(vendor_pandas, vendor_cal["sb"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "scs":
	    new_pandas = vendor.do_scs(vendor_pandas, vendor_cal["scs"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "trux":
	    new_pandas = vendor.do_trux(vendor_pandas, product_groups["trux"], vendor_cal["trux"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight", "Group Code"]
	    nelson_columns = titan_columns

	if vendor_name == "vms":
	    new_pandas = vendor.do_vms(vendor_pandas, vendor_cal["vms"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "warn":
	    new_pandas = vendor.do_warn(vendor_pandas, product_groups["warn"], vendor_cal["warn"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight", "Group Code"]
	    nelson_columns = titan_columns

	if vendor_name == "wes":
	    new_pandas = vendor.do_wes(vendor_pandas, product_groups["wes"], vendor_cal["wes"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight", "Group"]
	    nelson_columns = titan_columns

	if vendor_name == "west":
	    new_pandas = vendor.do_west(vendor_pandas, vendor_cal["west"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "yak":
	    new_pandas = vendor.do_yak(vendor_pandas, vendor_cal["yak"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	return new_pandas, titan_columns, nelson_columns
