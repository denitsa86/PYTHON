from payment_behavior_alaysis import find_the_last_day_current_month

def sum_current_due_invoices(open_invoices):
    if not open_invoices:
        return 0
    last_day = find_the_last_day_current_month()
    total = sum(inv.amount_in_usd for inv in open_invoices if inv.due_date < last_day)
    return total