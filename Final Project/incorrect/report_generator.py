# from openpyxl import Workbook
# import pandas as pd
#
# def sum_current_due_invoices(open_invoices):
#     if not open_invoices:
#         return 0
#
#     # Use the last day from any invoice object (same for all)
#     last_day = open_invoices[0].last_day_of_the_current_month
#
#     total = sum(inv.amount_in_usd for inv in open_invoices if inv.due_date < last_day)
#     return total
#
# def build_overdue_report_openpyxl(invoices, output_file="overdue_report.xlsx"):
#     # Filter invoices: only those due before the last day of the current month
#     last_day = invoices[0].last_day_of_the_current_month
#     filtered_invoices = [inv for inv in invoices if inv.due_date < last_day]
#
#     # Build DataFrame from filtered invoices
#     df = pd.DataFrame([{
#         "customer_name": inv.customer_name,
#         "customer_id": inv.customer_id,
#         "bucket": inv.bucket,
#         "amount_usd": inv.amount_in_usd
#     } for inv in filtered_invoices])
#
#     report_data = df.pivot_table(
#         index=["customer_name", "customer_id"],
#         columns="bucket",
#         values="amount_usd",
#         aggfunc="sum",
#         fill_value=0
#     )
#     # Add a total column
#     report_data["TotalUSD"] = report_data.sum(axis=1)
#
#     # Reset index so customer_name and customer_id become columns again
#     report_data = report_data.reset_index()
#
#     # Save directly to Excel
#     report_data.to_excel(output_file, sheet_name="MonthEndPrep", index=False)
#     print(f"Report saved to {output_file}")
#
# def build_overdue_report_by_status(invoices, output_file="overdue_report.xlsx"):
#     # Filter invoices: only those due before the last day of the current month
#     last_day = invoices[0].last_day_of_the_current_month
#     filtered_invoices = [inv for inv in invoices if inv.due_date < last_day]
#
#     # Build DataFrame from filtered invoices
#     df = pd.DataFrame([{
#         "customer_name": inv.customer_name,
#         "customer_id": inv.customer_id,
#         "status": inv.status,
#         "amount_usd": inv.amount_in_usd
#     } for inv in filtered_invoices])
#
#     report_data = df.pivot_table(
#         index=["customer_name", "customer_id"],
#         columns="status",
#         values="amount_usd",
#         aggfunc="sum",
#         fill_value=0
#     )
#     # Add a total column
#     report_data["TotalUSD"] = report_data.sum(axis=1)
#
#     # Reset index so customer_name and customer_id become columns again
#     report_data = report_data.reset_index()
#
#     # Save directly to Excel
#     report_data.to_excel(output_file, sheet_name="MonthEndPrepStatus", index=False)
#     print(f"Report saved to {output_file}")