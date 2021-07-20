#/usr/bin/python3

import openpyxl

wb = openpyxl.load_workbook('/mnt/c/temp/test.xlsx')
sheet = wb['Sheet1']

for i in range(1, 8):
    print(i, sheet.cell(row=i, column=1).value)

for i in range(1, 8):
    print(i, sheet.cell(row=i, column=1).value)
    if sheet.cell(row=i, column=1).value == '10.10.0.3':
        print("found")
        sheet.cell(row=i, column=1).value = None
        print("New value:", sheet.cell(row=i, column=1).value)
    else:
        print("Nothing found")
    #    sheet.cell(row=i, column=1).value = None
    #    print("Found value", sheet.cell(row=i, column=1).value
    #else:
    #    print("Nthonig found")
