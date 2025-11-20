from datetime import datetime, date
import pandas as pd
import calendar
from payment_behavior_analysis import find_the_last_day_current_month
from invoice_functions import convert_to_usd


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
        self.bucket = self.assign_to_overdue_bucket()
        self.amount_in_usd = convert_to_usd(self.amount, self.currency)
        self.last_day_of_the_current_month = find_the_last_day_current_month()
        #self.outstanding_amount_at_month_end = self.outstanding_on_month_end

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

    def outstanding_on_month_end(self, expected_payment_date):
        """
        Returns outstanding amount on D (day before last day of month).
        """
        if self.last_day_of_the_current_month < expected_payment_date:
            return self.amount
        else:
            return 0

    # # I have this also in data_load - to be fixed!!!
    # def convert_to_usd(self):
    #     rates = {"USD": 1.00, "EUR": 1.16, "GBP": 1.32, "TRY": 0.024, "PLN": 0.27, "DKK": 0.16}
    #     rate = rates.get(self.currency)  # , 1.0  -default to 1.0 if currency not found
    #     return round(self.amount * rate, 2)


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
        self.bucket = self.assign_to_overdue_bucket()
        self.amount_in_usd = convert_to_usd(self.amount, self.currency)

    def calculate_days_late(self):
        return (pd.to_datetime(self.payment_date).date() - self.due_date).days

    # # To be fixed - repeated code!!!
    # def convert_to_usd(self):
    #     rates = {"USD": 1.00, "EUR": 1.16, "GBP": 1.32, "TRY": 0.024, "PLN": 0.27, "DKK": 0.16}
    #     rate = rates.get(self.currency)  # , 1.0  -default to 1.0 if currency not found
    #     return round(self.amount * rate, 2)

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

#Classes have the same methods - to be fixed