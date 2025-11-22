import matplotlib.pyplot as plt
import pandas as pd
from invoice_functions import sum_current_due_invoices
from data_load import load_customers, load_open_invoices

""" For now I don`t plan to include the pie in the final report. I just wanted to exercise it"""

customers = load_customers("data folder/Customers.xlsx")
invoices = load_open_invoices("data folder/open invoices.XLSX")

# Group invoices by customer
totals = []
for cust in customers:
    cust_invoices = [inv for inv in invoices if inv.customer_id == cust.payer_number]
    total = sum_current_due_invoices(cust_invoices)
    totals.append({"Customer": cust.customer_name, "Total": total})

df = pd.DataFrame(totals)

# Sort and take top 10
top_customers = df.sort_values(by="Total", ascending=False).head(10)

# Build labels with both name and sum
labels = top_customers.apply(lambda row: f"{row['Customer']} ({row['Total']})", axis=1)

plt.pie(
    top_customers["Total"],
    labels=labels)
plt.show()
