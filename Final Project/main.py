from data_load import load_collectors, load_customers, load_open_invoices, load_closed_invoices
from payment_behavior_alaysis import average_days_late_per_customer, calculate_expected_date_open_invoices, \
    calculate_outstanding_at_month_end
from report_generator import build_reports

#load input data
collectors = load_collectors("data folder/Collectors.xlsx")
customer_to_collector = load_collectors("data folder/Collectors.xlsx")
customers = load_customers("data folder/Customers.xlsx")
open_invoices = load_open_invoices("data folder/open invoices.XLSX")
closed_invoices = load_closed_invoices("data folder/closed invoices.XLSX")

# Calculate average days late per customer
adl_by_customer = average_days_late_per_customer(closed_invoices)

# Calculate expected payment dates for open invoices
expected_payment = calculate_expected_date_open_invoices(open_invoices, adl_by_customer)

# Calculate outstanding totals at month end
outstanding_totals = calculate_outstanding_at_month_end(expected_payment, customers)

# generate reports in one file with different sheets
build_reports(open_invoices, customers, customer_to_collector, expected_payment, open_invoices, closed_invoices)
