# AAM Vendor Price Update

Set the python path so that it can find the import files in local directory...

`set PYTHONPATH=.`
  
Requires these Python modules (use pip to install)...
- pandas
- xlrd
- unidecode

To run the script use the following comand...

`python parts-list.py {name of price Excel file} {vendor name}`

To see a list of supported vendor namess, use the following command...

`python parts-list.py -h`

And the script should output something similar to this...

```usage: parts-list.py [-h] file vendor

Convert parts Excel file to a CSV formated file

positional arguments:
  file        Excel file
  vendor      Vendor name

optional arguments:
  -h, --help  show this help message and exit

The following Vendors are supported: tech, ard, tim, curt, fia, gor, knn, warn, rsp, kso, par, rig

