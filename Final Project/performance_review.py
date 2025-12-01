from datetime import date
import pandas as pd
from collections import defaultdict
from data_load import load_open_invoices, load_closed_invoices
from invoice_functions import sum_current_due_invoices
from payment_behavior_analysis import find_the_last_day_current_month

closed_invoices = load_closed_invoices("data folder/closed invoices.XLSX")
open_invoices = load_open_invoices("data folder/open invoices.XLSX")


# Calculate Total to be Collected for the current month
# total_to_be_collected would be sum of all open and closed invoices due from 1st day of the current
# month until last day - 1
def calculate_overall_performance(open_invoices, closed_invoices):
    today = date.today()
    last_day = find_the_last_day_current_month()
    first_day = date(today.year, today.month, 1)
    current_overdue_sum = sum_current_due_invoices(open_invoices)
    total_to_be_collected_closed = sum(
        inv.amount_in_usd
        for inv in closed_invoices
        if (first_day <= inv.due_date <= last_day) or
        (first_day <= pd.to_datetime(inv.payment_date).date() <= last_day)
    )

    total_to_be_collected = current_overdue_sum + total_to_be_collected_closed
    # Define the Target ---target is the overdue to be < 5%
    allowed_overdue = total_to_be_collected * 0.05
    current_overdue_percent = (current_overdue_sum / total_to_be_collected) * 100

    # Numeric results
    result = {
        "Month": today.strftime("%B %Y"),
        "Total To Be Collected USD": f"${total_to_be_collected:,.2f}",
        "Total Collected (Closed) USD": f"${total_to_be_collected_closed:,.2f}",
        "Allowed Overdue USD": f"${allowed_overdue:,.2f}",
        "Current OpenOverdue USD": f"${current_overdue_sum:,.2f}",
        "Current Overdue Percentage": f"{current_overdue_percent:.2f}%",
        "Target Reached": current_overdue_percent < 5.0,
        "Amount To Collect To Achieve Target USD": f"${max(0, current_overdue_sum - allowed_overdue):,.2f}"
    }
    # Clarification text (because people like to read text, not numbers)
    clarification = [
        f"--- Collection Performance for {today.strftime('%B %Y')} ---",
        f"Total to be Collected (Current Month): ${total_to_be_collected:,.2f}",
        f"Total Collected (closed): ${total_to_be_collected_closed:,.2f}",
        f"Maximum Allowed Overdue (5% Target): ${allowed_overdue:,.2f}",
        f"Current Open Overdue Amount To Be Collected: ${current_overdue_sum:,.2f}",
        f"Current Overdue Percentage: {current_overdue_percent:.2f}%",
    ]
    if current_overdue_percent < 5.0:
        clarification.append("** Target Reached! Current overdue is below 5%. **")
    else:
        clarification.append("** Target Not Reached. **")
        amount_to_collect_to_target = current_overdue_sum - allowed_overdue
        clarification.append(
            f"Amount to collect to reach target (<5%): ${amount_to_collect_to_target:,.2f}"
        )
    return result, clarification


