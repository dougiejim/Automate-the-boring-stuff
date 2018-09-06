
import openpyxl, pprint

print('Opening Spec_Masterfile...')

# Open the xlsx file and grab the first sheet.

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')

for columnNum in range(1, sheet.get_highest_column()):
    spreadText = open('Column ' + str(columnNum) +'.txt', 'a')
    for rowNum in range(2, sheet.get_highest_row()):
        rowData = sheet.cell(row=rowNum, column=columnNum).value
        spreadText.write(str(rowData) + '\n')
spreadText.close()
