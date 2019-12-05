import openpyxl as xl
# Add function
def Add():
    wb = xl.load_workbook('')  # write the spreedsheet(.xlsx) file name here you to Update
    sheet = wb['Sheet1']
    y = int(input("Enter the targeted row where value start: "))
    z = int(input("Enter the target column where these value belong: "))
    m = int(input("Enter where you want to import this Updated Value: "))
    for row in range(y, sheet.max_row + 1):
        x = int(input(f"Enter the value you want to Add for Row {row} with the origianl value: "))
        cell = sheet.cell(row, z)
        corrected_cell_price = cell.value + x
        corrected_cell = sheet.cell(row,m)
        corrected_cell.value = corrected_cell_price
    wb.save('')  # You can save the file formate with any name
