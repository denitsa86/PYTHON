from data_load import load_collectors, load_customers, load_open_invoices, load_closed_invoices
from payment_behavior_alaysis import average_days_late_per_customer, calculate_expected_date_open_invoices, \
    calculate_outstanding_at_month_end
from report_generator import build_reports

collectors = load_collectors("Collectors.xlsx")
customer_to_collector = load_collectors("collectors.xlsx")
customers = load_customers("Customers.xlsx")
open_invoices = load_open_invoices("open invoices.xlsx")
closed_invoices = load_closed_invoices("closed invoices.xlsx")
adl_by_customer = average_days_late_per_customer(closed_invoices)
# print("Average Days Late per Customer:")
# for customer_id, avg_days in adl_by_customer.items():
#     print(f"Customer {customer_id}: {avg_days:.2f} days")
expected_payment = calculate_expected_date_open_invoices(open_invoices, adl_by_customer)
# for item in expected_payment:
#     print(
#         f"Invoice {item['invoice_id']} | "
#         f"Customer {item['customer_id']} ({item['customer_name']}) | "
#         f"Due: {item['due_date']} | "
#         f"ADL: {item['adl']} days | "
#         f"Expected Payment: {item['expected_payment_date']} | "
#         f"Amount (USD): {item['amount_usd']}"
#     )
outstanding_totals = calculate_outstanding_at_month_end(expected_payment, customers)
# with open("outstanding_report.txt", "w") as f:
#     for customer_id, amount in outstanding_totals.items():
#         f.write(f"Customer {customer_id}: {amount:.2f}\n")

build_reports(open_invoices, customers, customer_to_collector, expected_payment)
