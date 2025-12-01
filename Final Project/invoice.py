import pandas as pd
from payment_behavior_analysis import find_the_last_day_current_month
from invoice_functions import convert_to_usd, assign_to_overdue_bucket
from datetime import datetime


class OpenInvoice:
    def __init__(self, status, invoice_id, customer_id, customer_name, invoice_date, due_date, amount,
                 document_currency,
                 co_code, profit_center):
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.due_date = pd.to_datetime(due_date).date()
        self.amount = amount
        self.currency = document_currency
        self.status = status
        self.co_code = co_code
        self.profit_center = profit_center
        self.invoice_date = invoice_date

        self.days_late = self.calculate_days_late()
        self.bucket = assign_to_overdue_bucket(self.days_late)
        self.amount_in_usd = convert_to_usd(self.amount, self.currency)

    def calculate_days_late(self):
        today = datetime.today().date()
        return (today - self.due_date).days


class ClosedInvoice:
    def __init__(self, status, invoice_id, customer_id, customer_name, invoice_date, due_date, amount,
                 document_currency,
                 co_code, profit_center, payment_date):
        self.status = status
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.due_date = pd.to_datetime(due_date).date()
        self.amount = amount
        self.currency = document_currency
        self.co_code = co_code
        self.profit_center = profit_center
        self.invoice_date = invoice_date
        self.payment_date = payment_date
        self.days_late = self.calculate_days_late()

        self.last_day_of_the_current_month = find_the_last_day_current_month()
        self.bucket = assign_to_overdue_bucket(self.days_late)
        self.amount_in_usd = convert_to_usd(self.amount, self.currency)

    def calculate_days_late(self):
        return (pd.to_datetime(self.payment_date).date() - self.due_date).days
