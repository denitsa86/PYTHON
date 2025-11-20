                     💰 CashMaster 💰

This program aims to help the Accounts Receivable team to:

✔️ Have better visibility of the whole portfolio and due amounts
within the current month
✔️ Identify risk in terms of cash collection
✔️ Improve and secure cash flow 

The problem is that the current software the team is using provides only 
current snapshot of the overdue amounts as of the current day. This is
not enough to be able to reach the target and keeping overdue < 5% at 
the current month end.

Rule: All invoices due until the day before the last day of the current 
month, should be collected/ paid latest on the last day of the month
(e.g. for November 2025: all invoices due until 29/11(incl. should be 
paid latest on 30/11) invoices due on 30/11 are considered for the 
next month-December).

Input data(xlsx files):
➕ Collectors: id + full name + manager(list of collectors, each 
responsible for list of customers /called portfolio or wallet/)
➕ Customers - number + name
➕ Account managers: name + customer + business segment (each account
manager is responsible for list of customers)
➕ Open invoices: Status + doc. number + doc. currency + amount in doc.
currency, document date + net due date + profit center(indicating the
line of business)
➕ Closed invoices: as open invoices + payment date

Fuctionality:
✅ Reads and loads input data from excel files -DONE
✅ Converts all amounts to USD - DONE/TO BE FIXED EVENTUALLY
✅ Aging analysis: prints report by overdue buckets (assign to overdue
bucket depending ot the due date and current day) - DONE
✅ Breaks down invoices by status and prints a report (collectors will
have full visibility on the status of their portfolio and prioritize
tasks if needed) - DONE
✅ Makes analysis of the payment behaviour of the customers (average days
late) and makes prognosis for possible overdue at the month end (payment
risk) - DONE
✅ Calculates the current performance of the team and if the target is 
reached (overdue < 5%) - DONE
✅ Calculate individual performance by collector - NOT DONE YET
✅ Include visualization (e.g. top 10 customers by due amount) - NOT 
DONE YET

NOTES:
❓Real-time currency convertion
❓Adjust the width and names of the columns in the reports
❓Think about edge cases
