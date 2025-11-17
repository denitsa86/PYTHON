from datetime import datetime
import pandas as pd
import calendar


class OpenInvoice:
    def __init__(self,status, invoice_id, customer_id, customer_name, invoice_date, due_date, amount, document_currency,
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
        # self.last_day_of_the_current_month = self.find_the_last_day_current_month()
        # self.bucket = self.assign_to_overdue_bucket()
    def calculate_days_late(self):
        today = datetime.today().date()
        return (today - self.due_date).days


class ClosedInvoice:
    def __init__(self, status, invoice_id, customer_id, customer_name, invoice_date, due_date, amount, document_currency,
                  co_code, profit_center, payment_date):
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
        self.payment_date = payment_date
        self.days_late = self.calculate_days_late()
        # self.last_day_of_the_current_month = self.find_the_last_day_current_month()
        # self.bucket = self.assign_to_overdue_bucket()

    def find_the_last_day_current_month(self):
        today = datetime.today()

        # monthrange() to gets the date range
        # year = 2025, month = 11
        result = calendar.monthrange(today.year, today.month)
        day = result[1] - 1  # last day is not considered for the curr.month
        return day

    def calculate_days_late(self):
        today = datetime.today().date()
        return (today - self.due_date).days

    def assign_to_overdue_bucket(self):
        if self.days_late <= 0:
            return "Not Due Yet"
        elif self.days_late <= 3:
            return "1-3"
        elif self.days_late <= 6:
            return "3-6"
        elif self.days_late <= 14:
            return "7-14"
        elif self.days_late <= 30:
            return "15-30"
        elif self.days_late <= 60:
            return "31-60"
        elif self.days_late <= 90:
            return "61-90"
        elif self.days_late <= 180:
            return "91-180"
        else:
            return "180+"
