# Run vendor processing and build columns
def vendor(vendor_pandas, vendor_cal, product_groups, vendor_name, vendor, discontinued, new_cal):
	titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4", "P5",
                     "Length", "Width", "Height", "Weight", "Status"]
	nelson_columns = titan_columns
	titan_columns_group = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
	                       "P5", "Length", "Width", "Height", "Weight", "Group Code"]

	if vendor_name == "3du":
	    new_pandas = vendor.do_3du(vendor_pandas, vendor_cal["3du"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3",
	                     "P4", "P5", "Length", "Width", "Height", "Weight"]

	if vendor_name == "aac":
	    new_pandas = vendor.do_aac(vendor_pandas, vendor_cal["aac"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3",
	                     "P4", "P5", "Length", "Width", "Height", "Weight"]

	if vendor_name == "aci":
	    new_pandas = vendor.do_aci(vendor_pandas, product_groups["aci"], vendor_cal["aci"])
	    # titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3",
	    #                  "P4", "P5", "Length", "Width", "Height", "Weight", "Group"]
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3",
	                     "P4", "P5", "Length", "Width", "Height", "Weight"]

	if vendor_name == "adu":
	    new_pandas = vendor.do_adu(vendor_pandas, vendor_cal["adu"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "airl":
	    new_pandas = vendor.do_airl(vendor_pandas, vendor_cal["airl"], new_cal)
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "and":
	    new_pandas = vendor.do_and(vendor_pandas, vendor_cal["and"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5"]
	    nelson_columns = titan_columns

	if vendor_name == "anz":
	    new_pandas = vendor.do_anz(vendor_pandas, vendor_cal["anz"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "amp":
	    new_pandas = vendor.do_amp(vendor_pandas, vendor_cal["amp"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns


	if vendor_name == "ampm":
	    new_pandas = vendor.do_ampm(vendor_pandas, vendor_cal["ampm"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "aor":
	    new_pandas = vendor.do_aor(vendor_pandas, product_groups["aor"], vendor_cal["aor"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3",
	                     "P4", "P5", "Length", "Width", "Height", "Weight", "Group Code"]
	    nelson_columns = titan_columns

	if vendor_name == "arb":
	    new_pandas = vendor.do_arb(vendor_pandas, vendor_cal["arb"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "arc":
	    new_pandas = vendor.do_arc(vendor_pandas, vendor_cal["arc"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "arcl":
	    new_pandas = vendor.do_arcl(vendor_pandas, vendor_cal["arcl"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "ard":
	    new_pandas = vendor.do_ard(vendor_pandas, vendor_cal["ard"])

	if vendor_name == "autc":
	    new_pandas = vendor.do_autc(vendor_pandas, vendor_cal["autc"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5"]
	    nelson_columns = titan_columns

	if vendor_name == "bak":
	    new_pandas = vendor.do_bak(vendor_pandas, vendor_cal["bak"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "baja":
	    new_pandas = vendor.do_baja(vendor_pandas, vendor_cal["baja"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "bap":
	    new_pandas = vendor.do_bap(vendor_pandas, vendor_cal["bap"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5"]
	    nelson_columns = titan_columns

	if vendor_name == "bdw":
	    new_pandas = vendor.do_bdw(vendor_pandas, vendor_cal["bdw"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3",
	                     "P4", "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "best":
	    new_pandas = vendor.do_best(vendor_pandas, vendor_cal["best"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3",
	                     "P4", "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "big":
	    new_pandas = vendor.do_big(vendor_pandas, product_groups["big"], vendor_cal["big"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3",
	                     "P4", "P5", "Length", "Width", "Height", "Weight", "Group"]
	    nelson_columns = titan_columns

	if vendor_name == "bigm":
	    new_pandas = vendor.do_bigm(vendor_pandas, product_groups["bigm"], vendor_cal["bigm"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3",
	                     "P4", "P5", "Length", "Width", "Height", "Weight", "Group"]
	    nelson_columns = titan_columns

	if vendor_name == "bil":
	    new_pandas = vendor.do_bil(vendor_pandas, vendor_cal["bil"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3",
	                     "P4", "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "bkr":
	    new_pandas = vendor.do_bkr(vendor_pandas, vendor_cal["bkr"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "brm":
	    new_pandas = vendor.do_brm(vendor_pandas, vendor_cal["brm"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "brug":
	    new_pandas = vendor.do_brug(vendor_pandas, vendor_cal["brug"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "btr":
	    new_pandas = vendor.do_btr(vendor_pandas, vendor_cal["btr"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Weight", "Group Code"]
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
	    new_pandas = vendor.do_tech(vendor_pandas, product_groups, vendor_cal["tech"], new_cal)
	    #                 new_part   part     descriptions     P1     P2      P3      P4    P5
	    titan_columns = ["NewPart", "Part", "Desc1", "Desc2", "P1", "P2", "P3", "P4", "P5",
	                     "Length", "Width", "Height", "Weight", "Group"]
	    nelson_columns =["NewPart", "Part", "Desc1", "Desc2", "P1", "P2", "P3", "P4", "NP5",
	                     "Length", "Width", "Height", "Weight", "Group"]

	if vendor_name == "tim":
	    new_pandas = vendor.do_tim(vendor_pandas, vendor_cal["tim"])
	    titan_columns = ["NewPart", "PART #", "Desc1", "Desc2", "P1", "P2", "P3", "P4", "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "carr":
	    new_pandas = vendor.do_carr(vendor_pandas, vendor_cal["carr"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "cbp":
	    new_pandas = vendor.do_cbp(vendor_pandas, vendor_cal["cbp"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "cipa":
	    new_pandas = vendor.do_cipa(vendor_pandas, vendor_cal["cipa"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5"]
	    nelson_columns = titan_columns

	if vendor_name == "cmf":
	    new_pandas = vendor.do_cmf(vendor_pandas, vendor_cal["cmf"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "cog":
	    new_pandas = vendor.do_cog(vendor_pandas, vendor_cal["cog"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "cov":
	    new_pandas = vendor.do_cov(vendor_pandas, vendor_cal["cov"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "crg":
	    new_pandas = vendor.do_crg(vendor_pandas, vendor_cal["crg"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "curt":
	    new_pandas = vendor.do_curt(vendor_pandas, vendor_cal["curt"])

	if vendor_name == "curtmap":
	    new_pandas = vendor.do_curtmap(vendor_pandas, vendor_cal["curt"])
	    titan_columns = ["NewPart", "P2"]
	    nelson_columns = titan_columns

	if vendor_name == "deck":
	    new_pandas = vendor.do_deck(vendor_pandas, vendor_cal["deck"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "dia":
	    new_pandas = vendor.do_dia(vendor_pandas, vendor_cal["dia"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "duha":
	    new_pandas = vendor.do_duha(vendor_pandas, vendor_cal["duha"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "ecco":
	    new_pandas = vendor.do_ecco(vendor_pandas, vendor_cal["ecco"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "edge":
	    new_pandas = vendor.do_edge(vendor_pandas, vendor_cal["edge"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "egr":
	    new_pandas = vendor.do_egr(vendor_pandas, vendor_cal["egr"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "ele":
	    new_pandas = vendor.do_ele(vendor_pandas, vendor_cal["ele"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "ext":
	    new_pandas = vendor.do_ext(vendor_pandas, vendor_cal["ext"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "extm":
	    new_pandas = vendor.do_extm(vendor_pandas, vendor_cal["ext"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "dez":
	    new_pandas = vendor.do_dez(vendor_pandas, vendor_cal["dez"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight", "Group Code"]
	    nelson_columns = titan_columns

	if vendor_name == "dom":
	    new_pandas = vendor.do_dom(vendor_pandas, product_groups["dom"], vendor_cal["dom"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight", "Group Code"]
	    nelson_columns = titan_columns

	if vendor_name == "f55":
	    new_pandas = vendor.do_f55(vendor_pandas, vendor_cal["f55"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "fac":
	    new_pandas = vendor.do_fac(vendor_pandas, vendor_cal["fac"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "federal":
	    new_pandas = vendor.do_federal(vendor_pandas, vendor_cal["federal"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "ffi":
	    new_pandas = vendor.do_ffi(vendor_pandas, vendor_cal["ffi"])
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

	if vendor_name == "fire":
	    new_pandas = vendor.do_fire(vendor_pandas, vendor_cal["fire"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "fish":
	    new_pandas = vendor.do_fish(vendor_pandas, vendor_cal["fish"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "fpm":
	    new_pandas = vendor.do_fpm(vendor_pandas, vendor_cal["fpm"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "golite":
	    new_pandas = vendor.do_golite(vendor_pandas, vendor_cal["golite"])
	    titan_columns = ["NewPart", "Part Number", "P1", "P2", "P3", "P4", "P5"]
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

	if vendor_name == "hus":
	    new_pandas = vendor.do_hus(vendor_pandas, vendor_cal["hus"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns
	    
	if vendor_name == "hyp":
	    new_pandas = vendor.do_hyp(vendor_pandas, vendor_cal["hyp"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns
	    
	if vendor_name == "ici":
	    new_pandas = vendor.do_ici(vendor_pandas, vendor_cal["ici"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns
	    
	if vendor_name == "kar":
	    new_pandas = vendor.do_kar(vendor_pandas, vendor_cal["kar"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns
	    
	if vendor_name == "kc":
	    new_pandas = vendor.do_kc(vendor_pandas, vendor_cal["kc"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns
	    
	if vendor_name == "kln":
	    new_pandas = vendor.do_kln(vendor_pandas, vendor_cal["kln"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "knk":
	    new_pandas = vendor.do_knk(vendor_pandas, product_groups["knk"], vendor_cal["knk"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Weight", "Group Code"]
	    # titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
      #                "P5", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "knkm":
	    new_pandas = vendor.do_knkm(vendor_pandas, vendor_cal["knkm"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Weight", "Group Code"]
	    nelson_columns = titan_columns

	if vendor_name == "knp":
	    new_pandas = vendor.do_knp(vendor_pandas, vendor_cal["knp"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2"]
	    nelson_columns = titan_columns

	if vendor_name == "knn":
	    new_pandas = vendor.do_knn(vendor_pandas, vendor_cal["knn"])

	if vendor_name == "lnd":
	    new_pandas = vendor.do_lnd(vendor_pandas, vendor_cal["lnd"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns
	    
	if vendor_name == "lift":
	    new_pandas = vendor.do_lift(vendor_pandas, vendor_cal["lift"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "luv":
	    new_pandas = vendor.do_luv(vendor_pandas, vendor_cal["luv"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "mag":
	    new_pandas = vendor.do_mag(vendor_pandas, vendor_cal["mag"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "mas":
	    new_pandas = vendor.do_mas(vendor_pandas, vendor_cal["mas"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "mass":
	    new_pandas = vendor.do_mass(vendor_pandas, vendor_cal["mass"])
	    # titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4", "P5"]
	    # titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4", "P5"] # Tech
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4", "P5", "Profit"] # FED
	    # titan_columns = ["NewPart", "Desc1", "Desc2", "Status"] # WES
	    nelson_columns = titan_columns

	if vendor_name == "maxx":
	    new_pandas = vendor.do_maxx(vendor_pandas, vendor_cal["maxx"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5"]
	    nelson_columns = titan_columns

	if vendor_name == "mba":
	    new_pandas = vendor.do_mba(vendor_pandas, vendor_cal["mba"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "mrw":
	    new_pandas = vendor.do_mrw(vendor_pandas, vendor_cal["mrw"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                      "P5", "Length", "Width", "Height", "Weight"]
	    # titan_columns = ["NewPart", "Part Number", "P1", "P2", "P3", "P4", "P5"]
	    nelson_columns = titan_columns

	if vendor_name == "myp":
	    new_pandas = vendor.do_myp(vendor_pandas, vendor_cal["myp"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "nfa":
	    new_pandas = vendor.do_nfa(vendor_pandas, vendor_cal["nfa"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "nitro":
	    new_pandas = vendor.do_nitro(vendor_pandas, vendor_cal["nitro"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "odr":
	    new_pandas = vendor.do_odr(vendor_pandas, vendor_cal["odr"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "orl":
	    new_pandas = vendor.do_orl(vendor_pandas, vendor_cal["orl"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "ovs":
	    new_pandas = vendor.do_ovs(vendor_pandas, vendor_cal["ovs"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "pc":
	    new_pandas = vendor.do_pc(vendor_pandas, vendor_cal["pc"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "piaa":
	    new_pandas = vendor.do_piaa(vendor_pandas, vendor_cal["piaa"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3",
	                     "P4", "P5", "Length", "Width", "Height", "Weight", "Group"]
	    nelson_columns = titan_columns

	if vendor_name == "phoe":
	    new_pandas = vendor.do_phoe(vendor_pandas, vendor_cal["phoe"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3",
	                     "P4", "P5"]
	    nelson_columns = titan_columns

	if vendor_name == "pj":
	    new_pandas = vendor.do_pj(vendor_pandas, vendor_cal["pj"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3",
	                     "P4", "P5"]

	if vendor_name == "pull":
	    new_pandas = vendor.do_pull(vendor_pandas, vendor_cal["pull"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5"]
	    nelson_columns = titan_columns

	if vendor_name == "protec":
	    new_pandas = vendor.do_protec(vendor_pandas, vendor_cal["protec"], new_cal)
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4", "P5"]
	    nelson_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "NP1", "NP2", "NP3", "NP4", "NP5"]

	if vendor_name == "qf":
	    new_pandas = vendor.do_qf(vendor_pandas, vendor_cal["qf"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
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

	if vendor_name == "put":
	    new_pandas = vendor.do_put(vendor_pandas, vendor_cal["put"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "rcs":
	    new_pandas = vendor.do_rcs(vendor_pandas, vendor_cal["rcs"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight", "Group Code"]
	    nelson_columns = titan_columns

	if vendor_name == "rch":
	    new_pandas = vendor.do_rch(vendor_pandas, vendor_cal["rch"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "rdl":
	    new_pandas = vendor.do_rdl(vendor_pandas, vendor_cal["rdl"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "rfn":
	    new_pandas = vendor.do_rfn(vendor_pandas, vendor_cal["rfn"], new_cal)
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "rgr":
	    new_pandas = vendor.do_rgr(vendor_pandas, vendor_cal["rgr"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "rig":
	    new_pandas = vendor.do_rig(vendor_pandas, vendor_cal["rig"])

	if vendor_name == "rlg":
	    new_pandas = vendor.do_rlg(vendor_pandas, vendor_cal["rlg"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "rnl":
	    new_pandas = vendor.do_rnl(vendor_pandas, vendor_cal["rnl"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "road":
	    new_pandas = vendor.do_road(vendor_pandas, vendor_cal["road"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "ros":
	    new_pandas = vendor.do_ros(vendor_pandas, vendor_cal["ros"])
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

	if vendor_name == "rtx":
	    new_pandas = vendor.do_rtx(vendor_pandas, vendor_cal["rtx"])
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

	if vendor_name == "sky":
	    new_pandas = vendor.do_sky(vendor_pandas, vendor_cal["sky"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "sls":
	    new_pandas = vendor.do_sls(vendor_pandas, vendor_cal["sls"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "snow":
	    new_pandas = vendor.do_snow(vendor_pandas, vendor_cal["snow"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "stlc":
	    new_pandas = vendor.do_stlc(vendor_pandas, vendor_cal["stlc"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "sup":
	    new_pandas = vendor.do_sup(vendor_pandas, vendor_cal["sup"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "tfi":
	    new_pandas = vendor.do_tfi(vendor_pandas, vendor_cal["tfi"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "tfp":
	    new_pandas = vendor.do_tfp(vendor_pandas, vendor_cal["tfp"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "tft":
	    new_pandas = vendor.do_tft(vendor_pandas, vendor_cal["tft"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "tgp":
	    new_pandas = vendor.do_tgp(vendor_pandas, vendor_cal["tgp"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "tom":
	    new_pandas = vendor.do_tom(vendor_pandas, vendor_cal["tom"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "GL", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "t-rex":
	    new_pandas = vendor.do_trex(vendor_pandas, vendor_cal["t-rex"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "trm":
	    new_pandas = vendor.do_trm(vendor_pandas, vendor_cal["trm"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "trux":
	    new_pandas = vendor.do_trux(vendor_pandas, product_groups["trux"], vendor_cal["trux"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight", "Group Code"]
	    nelson_columns = titan_columns

	if vendor_name == "truxm":
	    new_pandas = vendor.do_truxm(vendor_pandas, product_groups["trux"], vendor_cal["truxm"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "ult":
	    new_pandas = vendor.do_ult(vendor_pandas, vendor_cal["ult"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5"]
	    nelson_columns = titan_columns

	if vendor_name == "und":
	    new_pandas = vendor.do_und(vendor_pandas, vendor_cal["und"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "uws":
	    new_pandas = vendor.do_uws(vendor_pandas, product_groups["uws"], vendor_cal["uws"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight", "Group Code"]
	    nelson_columns = titan_columns

	if vendor_name == "uwsb":
	    new_pandas = vendor.do_uwsb(vendor_pandas, vendor_cal["uwsb"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "ven":
	    new_pandas = vendor.do_ven(vendor_pandas, vendor_cal["ven"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "vms":
	    new_pandas = vendor.do_vms(vendor_pandas, vendor_cal["vms"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5"]
	    nelson_columns = titan_columns

	if vendor_name == "warn":
	    new_pandas = vendor.do_warn(vendor_pandas, vendor_cal["warn"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight", "Group_Code"]
	    nelson_columns = titan_columns

	if vendor_name == "wes":
	    new_pandas = vendor.do_wes(vendor_pandas, product_groups["wes"], vendor_cal["wes"], new_cal)
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight", "Group Code"]
	    nelson_columns = titan_columns

	if vendor_name == "west":
	    new_pandas = vendor.do_west(vendor_pandas, vendor_cal["west"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight", "Group_Code"]
	    # titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
      #               "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "wick":
	    new_pandas = vendor.do_wick(vendor_pandas, vendor_cal["wick"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "wig":
	    new_pandas = vendor.do_wig(vendor_pandas, vendor_cal["wig"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "xan":
	    new_pandas = vendor.do_xan(vendor_pandas, vendor_cal["xan"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5"]
	    nelson_columns = titan_columns

	if vendor_name == "yak":
	    new_pandas = vendor.do_yak(vendor_pandas, vendor_cal["yak"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	if vendor_name == "zll":
	    new_pandas = vendor.do_zll(vendor_pandas, vendor_cal["zll"])
	    titan_columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4",
                     "P5", "Length", "Width", "Height", "Weight"]
	    nelson_columns = titan_columns

	return new_pandas, titan_columns, nelson_columns
