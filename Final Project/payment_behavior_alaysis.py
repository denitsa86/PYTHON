from customer import Customer
from collector import Collector
from account_manager import AccountManager
from invoice import OpenInvoice
from invoice import ClosedInvoice
from datetime import datetime
import pandas as pd
from data_load import load_closed_invoices
from report_generator import average_days_late_per_customer

closed_invoices = load_closed_invoices("closed invoices.xlsx")
adl_by_customer = average_days_late_per_customer(closed_invoices)

for customer, adl in adl_by_customer.items():
    print(f"Customer {customer}: ADL = {adl:.2f} days")


