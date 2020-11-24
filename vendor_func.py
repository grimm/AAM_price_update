# Import vender functions

def vendor_func(vendor_name):
	if vendor_name == "tech":
	    import vendor.tech as vendor
	elif vendor_name == "aci":
	    import vendor.aci as vendor
	elif vendor_name == "ard":
	    import vendor.ard as vendor
	elif vendor_name == "adu":
	    import vendor.adu as vendor
	elif vendor_name == "tim":
	    import vendor.tim as vendor
	elif vendor_name == "curt":
	    import vendor.curt as vendor
	elif vendor_name == "fia":
	    import vendor.fia as vendor
	elif vendor_name == "gor":
	    import vendor.gor as vendor
	elif vendor_name == "knn":
	    import vendor.knn as vendor
	elif vendor_name == "nfa":
	    import vendor.nfa as vendor
	elif vendor_name == "warn":
	    import vendor.warn as vendor
	elif vendor_name == "rsp":
	    import vendor.rsp as vendor
	elif vendor_name == "kso":
	    import vendor.kso as vendor
	elif vendor_name == "par":
	    import vendor.par as vendor
	elif vendor_name == "piaa":
	    import vendor.piaa as vendor
	elif vendor_name == "protec":
	    import vendor.protec as vendor
	elif vendor_name == "rig":
	    import vendor.rig as vendor
	elif vendor_name == "gorm":
	    import vendor.gorm as vendor
	elif vendor_name == "yak":
	    import vendor.yak as vendor

	return vendor
