from openpyxl import Workbook
from collections import defaultdict


def build_overdue_report_openpyxl(invoices, output_file="overdue_report.xlsx"):
    # Step 1: aggregate data
    report_data = defaultdict(lambda: defaultdict(float))

    for inv in invoices:
        key = (inv.customer_name, inv.customer_id)  # you can also add collector/manager here
        report_data[key][inv.bucket] += inv.amount  # assumes already converted to USD

    # Step 2: create workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "MonthEndPrep"

    # Step 3: write headers
    headers = ["Customer Name", "Customer ID", "Not Due Yet", "1-3", "3-6", "7-14",
               "15-30", "31-60", "61-90", "91-180", "180+", "TotalUSD"]
    ws.append(headers)

    # Step 4: write rows
    for (cust_name, cust_id), buckets in report_data.items():
        row = [cust_name, cust_id]
        total = 0
        for bucket in headers[2:-1]:  # skip first two and last column
            val = buckets.get(bucket, 0)
            row.append(val)
            total += val
        row.append(total)
        ws.append(row)

    # Step 5: save workbook
    wb.save(output_file)
    print(f"Report saved to {output_file}")
