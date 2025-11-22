from payment_behavior_analysis import find_the_last_day_current_month

def sum_current_due_invoices(open_invoices):
    if not open_invoices:
        return 0
    last_day = find_the_last_day_current_month()
    total = sum(inv.amount_in_usd for inv in open_invoices if inv.due_date <= last_day)
    return total

def convert_to_usd(amount,currency):
    rates = {"USD": 1.00, "EUR": 1.16, "GBP": 1.32, "TRY": 0.024, "PLN": 0.27, "DKK": 0.16}
    rate = rates.get(currency.upper())  # if currency not found ??
    if rate is None:
        raise ValueError(f"Unsupported currency: {currency}")
    try:
        return round(float(amount) * rate, 2)
    except (TypeError, ValueError):
        raise ValueError(f"Invalid amount: {amount}")

def assign_to_overdue_bucket(days_late): # int - str:
    #Assigns an invoice to an overdue bucket based on days late.
    if days_late <= 0:
        return "Not Due Yet"
    elif days_late <= 3:
        return "1-3"
    elif days_late <= 6:
        return "4-6"
    elif days_late <= 14:
        return "7-14"
    elif days_late <= 30:
        return "15-30"
    elif days_late <= 60:
        return "31-60"
    elif days_late <= 90:
        return "61-90"
    elif days_late <= 180:
        return "91-180"
    else:
        return "180+"
