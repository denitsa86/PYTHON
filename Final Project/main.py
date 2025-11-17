from data_load import load_collectors, load_customers, load_open_invoices
#from report_generator import build_overdue_report_openpyxl, build_overdue_report_by_status
from report_generator import build_reports

collectors = load_collectors("Collectors.xlsx")
customer_to_collector = load_collectors("collectors.xlsx")
customers = load_customers("Customers.xlsx")
open_invoices = load_open_invoices("open invoices.xlsx")
# convert_to_usd("open invoices.xlsx","open invoices converted.xlsx")
# calculate_days_late("open invoices.xlsx","open invoices converted.xlsx")
# build_overdue_report_openpyxl(open_invoices)
# build_overdue_report_by_status(open_invoices)
build_reports(open_invoices, customer_to_collector)

