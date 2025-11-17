import pandas as pd
from collections import defaultdict


def sum_current_due_invoices(open_invoices):
    if not open_invoices:
        return 0
    last_day = open_invoices[0].last_day_of_the_current_month
    total = sum(inv.amount_in_usd for inv in open_invoices if inv.due_date < last_day)
    return total


def build_reports(invoices, customer_to_collector, output_file="overdue_report.xlsx"):
    # Common filter
    last_day = invoices[0].last_day_of_the_current_month
    filtered_invoices = [inv for inv in invoices if inv.due_date < last_day]

    # --- First report: by bucket ---
    df_bucket = pd.DataFrame([{
        "customer_name": inv.customer_name,
        "customer_id": inv.customer_id,
        "bucket": inv.bucket,
        "amount_usd": inv.amount_in_usd,
        "collector_name": customer_to_collector.get(inv.customer_id, ("Unknown", ""))[0],
        "collector_manager": customer_to_collector.get(inv.customer_id, ("Unknown", ""))[1]
    } for inv in filtered_invoices])

    report_bucket = df_bucket.pivot_table(
        index=["customer_name", "customer_id", "collector_name", "collector_manager"],
        columns="bucket",
        values="amount_usd",
        aggfunc="sum",
        fill_value=0
    )
    report_bucket["TotalUSD"] = report_bucket.sum(axis=1)
    report_bucket = report_bucket.reset_index()

    # --- Second report: by status ---
    df_status = pd.DataFrame([{
        "customer_name": inv.customer_name,
        "customer_id": inv.customer_id,
        "status": inv.status,
        "amount_usd": inv.amount_in_usd
    } for inv in filtered_invoices])

    report_status = df_status.pivot_table(
        index=["customer_name", "customer_id"],
        columns="status",
        values="amount_usd",
        aggfunc="sum",
        fill_value=0
    )
    report_status["TotalUSD"] = report_status.sum(axis=1)
    report_status = report_status.reset_index()

    # --- Write both to the same Excel file ---
    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        report_bucket.to_excel(writer, sheet_name="AgingReport", index=False)
        report_status.to_excel(writer, sheet_name="MonthEndPrepStatus", index=False)

    print(f"Reports saved to {output_file} with two sheets.")


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
