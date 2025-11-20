import pandas as pd
from openpyxl import load_workbook
from payment_behavior_analysis import find_the_last_day_current_month, calculate_outstanding_at_month_end
from performance_review import calculate_overall_performance


def build_reports(invoices, customers, customer_to_collector, expected_dates, open_invoices,
                  closed_invoices, output_file="overdue_report.xlsx"):
    # Common filter
    last_day = find_the_last_day_current_month()
    filtered_invoices = [inv for inv in invoices if inv.due_date < last_day]

    # --- First report: by overdue bucket ---
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
        "amount_usd": inv.amount_in_usd,
        "collector_name": customer_to_collector.get(inv.customer_id, ("Unknown", ""))[0],
    } for inv in filtered_invoices])

    report_status = df_status.pivot_table(
        index=["customer_name", "customer_id", "collector_name"],
        columns="status",
        values="amount_usd",
        aggfunc="sum",
        fill_value=0
    )
    report_status["TotalUSD"] = report_status.sum(axis=1)
    report_status = report_status.reset_index()

    # --- Third report: expected overdue on D ---

    outstanding_by_customer = calculate_outstanding_at_month_end(expected_dates, customers)

    df_outstanding = pd.DataFrame([{
        "customer_id": cust_id,
        "customer_name": next(
            (cust.customer_name for cust in customers if cust.payer_number == cust_id),
            "Unknown"
        ),
        "collector_name": customer_to_collector.get(cust_id, ("Unknown", ""))[0],
        "collector_manager": customer_to_collector.get(cust_id, ("Unknown", ""))[1],
        "ExpectedOverdueUSD": amount
    } for cust_id, amount in outstanding_by_customer.items()
        if amount > 0  # only include customers with outstanding balance
    ])

    report_expected = df_outstanding.groupby(
        ["customer_name", "customer_id", "collector_name", "collector_manager"], as_index=False
    )["ExpectedOverdueUSD"].sum()

    # --- 4th report overall performance ---

    performance_result, clarification = calculate_overall_performance(open_invoices, closed_invoices)
    df_performance = pd.DataFrame([performance_result])

    # --- Write all in the same Excel file ---
    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        report_bucket.to_excel(writer, sheet_name="AgingReport", index=False)
        report_status.to_excel(writer, sheet_name="MonthEndPrepStatus", index=False)
        report_expected.to_excel(writer, sheet_name="ExpectedOverdueOnMonthEnd", index=False)
        df_performance.to_excel(writer, sheet_name="PerformanceSummary", index=False)

    # --- Append custom text to the third sheet ---
    wb = load_workbook(output_file)
    ws = wb["ExpectedOverdueOnMonthEnd"]
    last_row = ws.max_row + 2  # Leave a blank row
    ws.cell(row=last_row,
            column=1).value = "PLEASE FOCUS ON THESE CUSTOMERS. THERE IS A LATE PAYMENT EXPECTED THIS MONTH!"
    # --- Append clarifications to the fourth sheet ---
    ws_perf = wb["PerformanceSummary"]
    last_row_perf = ws_perf.max_row + 2
    ws_perf.cell(row=last_row_perf, column=1).value = "Clarifications:"
    for i, line in enumerate(clarification, start=1):
        ws_perf.cell(row=last_row_perf + i, column=1).value = line
    wb.save(output_file)

    print(f"Reports saved to {output_file} with 4 sheets.")
