from data_load import load_closed_invoices, load_open_invoices
from collections import defaultdict
from datetime import timedelta, date, datetime
import calendar


# find the day before the last day of the current month! This is considered as last day of the month.
def find_the_last_day_current_month():
    today = datetime.today()
    last_day = calendar.monthrange(today.year, today.month)[1]  # last day number
    return date(today.year, today.month, last_day - 1)  # full date object


# analyze days late in closed invoices and find average
def average_days_late_per_customer(closed_invoices):
    # dictionary to hold totals and counts
    customer_stats = defaultdict(lambda: {"total_days": 0, "count": 0})

    for inv in closed_invoices:
        customer = inv.customer_id
        customer_stats[customer]["total_days"] += inv.days_late
        customer_stats[customer]["count"] += 1

    # compute averages
    adl_per_customer = {
        cust: stats["total_days"] / stats["count"]
        for cust, stats in customer_stats.items()
    }
    return adl_per_customer


# prognosed payment date based on ADL
def calculate_expected_date_open_invoices(open_invoices, adl_by_customer):
    expected_dates = []
    last_day = find_the_last_day_current_month()
    # Debug check: inspect each invoice before filtering
    # with open("invoice_debug.txt", "w") as f:
    #     print(len(open_invoices))
    #     for inv in open_invoices:
    #         f.write(
    #             f"Invoice {inv.invoice_id} | "
    #             f"Due: {inv.due_date} ({type(inv.due_date).__name__}) | "
    #             f"<= last_day? {inv.due_date <= last_day}\n"
    #         )

    filtered_invoices = [inv for inv in open_invoices if
                         inv.due_date <= last_day]  # taking into consideration only onv for current month

    for inv in filtered_invoices:
        customer = inv.customer_id
        due_date = inv.due_date
        adl = adl_by_customer.get(customer, 0)
        expected_date = due_date + timedelta(days=adl)

        expected_dates.append({
            "invoice_id": inv.invoice_id,
            "customer_id": customer,
            "customer_name": inv.customer_name,
            "due_date": due_date,
            "adl": adl,
            "expected_payment_date": expected_date,
            "amount_usd": inv.amount_in_usd
        })

    return expected_dates


# calculate prognosed outstanding amount at month end
def calculate_outstanding_at_month_end(expected_dates, customers):
    last_day = find_the_last_day_current_month()

    # Initialize all customers with 0 outstanding
    outstanding_by_customer = {cust.payer_number: 0.0 for cust in customers}

    for entry in expected_dates:
        expected_payment_date = entry["expected_payment_date"]

        # If expected payment date is after D, invoice is still outstanding
        if expected_payment_date > last_day:
            payer_number = entry["customer_id"]
            if payer_number not in outstanding_by_customer:
                outstanding_by_customer[payer_number] = 0.0
            outstanding_by_customer[payer_number] += entry["amount_usd"]

    return outstanding_by_customer
