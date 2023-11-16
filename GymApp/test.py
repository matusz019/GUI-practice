import openpyxl

# Create a new Workbook object
workbook = openpyxl.Workbook()

# Get the active sheet (the first sheet by default)
sheet = workbook.active

# Add data to cells
sheet['A1'] = 'Name'
sheet['B1'] = 'Age'
sheet['A2'] = 'Alice'
sheet['B2'] = 30
sheet['A3'] = 'Bob'
sheet['B3'] = 35

# Save the workbook to a file
workbook.save('example.xlsx')

print("Data written successfully to 'example.xlsx'")

