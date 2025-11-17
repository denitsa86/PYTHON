import os
import pandas as pd

count = 100500
start = 1

invoice_numbers = []
for i in range(count):
    # Invoice number with zero-padding
    invoice_number = str(start + i).zfill(9)
    invoice_numbers.append(invoice_number)

# Create DataFrame
df = pd.DataFrame({"Document Number": invoice_numbers})

# Save to Excel
df.to_excel("invoices.xlsx", index=False)

print(os.getcwd())
