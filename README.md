This script takes a AAM vendor (and other vendors) Excel file and process/converts it to a CSV (pipe seperated) file that can be ingested into the FACS system.  The initial instructions here are for setting up the Python environment.

Set the python path so that it can find the import files in local directory...

`set PYTHONPATH=.`
  
Requires these Python modules (use pip to install)...
- pandas
- xlrd
- unidecode
- pyyaml
- os

If running on Linux this script requires the following software to function...
- dos2unix

To run the script use the following comand...

`py conv_price.py {name of price Excel file} {vendor name}`

To see a list of supported vendor namess, use the following command...

`py conv_price.py -h`

And the script should output something similar to this...

```usage: conv_price.py [-h] [-d] [-n] file vendor

The mass vendor is used to import data from the FACS mass report

positional arguments:
  file        Excel file
  vendor      Vendor Product Code

optional arguments:
  -h, --help  show this help message and exit
  -d          Process all parts as discontinued
  -n          Do new calculation

The following 90 Vendor product codes are supported: aci, adu, airl, and, anz, amp, ampm, aor, arb, arcl, ard, baja,
bak, bap, best, big, bigm, bkr, brm, bush, buy, carr, cbp, cipa, crg, curt, deck, dez, eccon, eccot, ffi, fia, fil,
fire, fpm, gor, gorm, hus, kar, kc, knk, knkm, knn, kso, lift, mas, mass, mba, mrw, myp, nfa, nitro, odr, ovs, par,
piaa, prime, protec, put, qf, rch, rcs, rdl, rfn, rgr, rig, rlg, road, rrk, rsp, rtx, rug, sb, scs, sls, snow, stlc,
tech, tim, t-rex, trux, und, uws, uwsb, ven, vms, warn, wes, west, yak

