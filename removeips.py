#/usr/bin/python3

#take a spreadsheet of IP addresses, check for and remove certain IPs from a .txt file
#spreadsheet must have the sheet named Sheet1

import openpyxl #module for working with excel files

input_workbook = input("Enter exact path of Excel file to read: ")
input_ipremovelist = input("Enter exact path of IP remove list: ")
wb = openpyxl.load_workbook(input_workbook)

sheet = wb['Sheet1'] #set the active sheet; only works with default single sheet Sheet1 for now
ipremove_list = input_ipremovelist
#ipremove_list = r'C:\path\ipstoremove.txt' #need to use r'path to treat as raw string, \ will cause char encoding error otherwise

try:
    with open(ipremove_list) as ipremovelist_file:
        for line in ipremovelist_file:
            for i in range(1, sheet.max_row + 1): #adjust for missing last line
                line = line.strip() #built in method to remove whitespace from strings
                if sheet.cell(row=i, column=1).value == line: #find each instance of IPs to remove starting at row i (1) and going through range
                    sheet.delete_rows(i) #delete the rows with the found IP
except: #generic error catching
    print("Something does not work")

wb.save(r'.\output.xlsx') #save result as new excel file
print("Output saved to output.xlsx")
input("Press <ENTER> to exit")
