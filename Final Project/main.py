from data_load import load_collectors, load_customers, load_open_invoices, load_closed_invoices
from payment_behavior_analysis import average_days_late_per_customer, calculate_expected_date_open_invoices
from report_generator import build_reports


def main():
    # load input data
    collectors = load_collectors("data folder/Collectors.xlsx")
    customers = load_customers("data folder/Customers.xlsx")
    open_invoices = load_open_invoices("data folder/open invoices.XLSX")
    closed_invoices = load_closed_invoices("data folder/closed invoices.XLSX")

    # Calculate average days late per customer
    adl_by_customer = average_days_late_per_customer(closed_invoices)

    # Calculate expected payment dates for open invoices
    expected_payment = calculate_expected_date_open_invoices(open_invoices, adl_by_customer)

    # generate reports in one file with different sheets
    build_reports(customers, collectors, expected_payment,open_invoices, closed_invoices)


if __name__ == "__main__":
    main()
