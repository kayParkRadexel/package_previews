import pydicom as pdcm
from pydicom.data import get_testdata_file

test1 = get_testdata_file("rtplan.dcm")
ds = pdcm.dcmread(test1)

print(ds[0x8, 0x1010].keyword)
print(ds[0x8, 0x1010].value)
