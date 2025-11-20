from payment_behavior_analysis import find_the_last_day_current_month

def sum_current_due_invoices(open_invoices):
    if not open_invoices:
        return 0
    last_day = find_the_last_day_current_month()
    total = sum(inv.amount_in_usd for inv in open_invoices if inv.due_date < last_day)
    return total

def convert_to_usd(amount,currency):
    rates = {"USD": 1.00, "EUR": 1.16, "GBP": 1.32, "TRY": 0.024, "PLN": 0.27, "DKK": 0.16}
    rate = rates.get(currency)  # if currency not found ??
    return round(amount * rate, 2)