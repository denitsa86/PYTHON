from data_load import load_collectors, load_customers, load_open_invoices, convert_to_usd

collectors = load_collectors("Collectors.xlsx")
customers = load_customers("Customers.xlsx")
open_invoices = load_open_invoices("open invoices.xlsx")
for invoice in open_invoices:
    invoice["amount_usd"] = convert_to_usd(invoice["amount"], invoice["currency"])

