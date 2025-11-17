from customer import Customer
from collector import Collector
from account_manager import AccountManager
from invoice import OpenInvoice
from invoice import ClosedInvoice
from datetime import datetime
from data_load import load_closed_invoices

closed_invoices = load_closed_invoices("closed invoices.xlsx")
def calculate_average_days_late(invoices, days_late):
    average_days_late = days_late / len(invoices)
    return average_days_late
calculate_average_days_late(closed_invoices)
