"""openpyxl - A Python library to read/write Excel 2010 xlsx/xlsm files
openpyxl is a Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files.
rom openpyxl import Workbook
wb = Workbook()

# grab the active worksheet
ws = wb.active

# Data can be assigned directly to cells
ws['A1'] = 42

# Rows can also be appended
ws.append([1, 2, 3])

# Python types will automatically be converted
import datetime
ws['A2'] = datetime.datetime.now()

# Save the file
wb.save("sample.xlsx")


Key Features of OpenPyxl
Read and Write Excel Files: OpenPyxl can be used to both read from and write to .xlsx files.
Work with Cells: We can access, modify, and create new cells in Excel sheets.
Support for Formulas: OpenPyxl supports the evaluation of Excel formulas.
Styles and Formatting: We can modify the look and feel of cells (font, color, borders, etc.).
Charting: OpenPyxl also provides the ability to create simple charts in Excel files.
Working with Pivot Tables: Though limited, OpenPyxl offers the capability to interact with pivot tables.
"""