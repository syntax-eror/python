#!/usr/bin/env python3

import openpyxl #pip3 install openpyxl

wb = openpyxl.load_workbook('/mnt/c/temp/test.xlsx') #replace with var
sheet = wb['Sheet1'] #can call specific sheets in a wb; Sheet1 is the default
cella1 = sheet['A1']
print(cella1.value)
