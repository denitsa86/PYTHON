from data_load import load_collectors, load_customers, load_open_invoices

collectors = load_collectors("Collectors.xlsx")
customers = load_customers("Customers.xlsx")
open_invoices = load_open_invoices("open invoices.xlsx")
open_invoices.convert_to_usd()

