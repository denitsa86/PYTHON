import pandas as pd
from customer import Customer
from collector import Collector
from account_manager import AccountManager
from invoice import OpenInvoice, ClosedInvoice


# load customers
def load_customers(filename="customers.xlsx"):
    try:
        df = pd.read_excel(filename)
    except FileNotFoundError:
        print(f"File {filename} not found")
        return []
    return [Customer(row["Payer number"], row["Customer Name"]) for _, row in df.iterrows()]


# load collectors/assign customer to collector.
def load_collectors(filename="collectors.xlsx"):
    try:
        df = pd.read_excel(filename)
    except FileNotFoundError:
        print(f"File {filename} not found")
        return []
    collectors = {}
    for _, row in df.iterrows():
        coll_name = row["Collector Full Name"]
        manager = row["Manager"]
        cust_id = row["Payer number"]

        if coll_name not in collectors:
            collectors[coll_name] = Collector(coll_name, manager)
        collectors[coll_name].assign_customer(cust_id)

    # Build lookup: customer_id → (collector_name, manager)
    customer_to_collector = {}
    for collector in collectors.values():
        for cust in collector.customers:
            customer_to_collector[cust] = (collector.collector_name, collector.collector_manager)

    return customer_to_collector

#
# # Load account managers
# def load_account_managers(filename="account_managers.xlsx"):
#     try:
#         df = pd.read_excel(filename)
#     except FileNotFoundError:
#         print(f"File {filename} not found")
#         return []
#     return [AccountManager(row["Account Manager"], row["Business segment"], row["Managed Payer"]) for _, row in
#             df.iterrows()]


# load open invoices
def load_open_invoices(filename="open invoices.xlsx"):
    try:
        df = pd.read_excel(filename)
    except FileNotFoundError:
        print(f"File {filename} not found")
        return []
    invoices = []
    for _, row in df.iterrows():
        invoice = OpenInvoice(
            status=row["Status"],
            customer_id=row["Payer number"],
            customer_name=row["Customer Name"],
            co_code=row["Company Code"],
            invoice_date=row["Document Date"],
            due_date=row["Net due date"],
            document_currency=row["Document currency"],
            amount=row["Amount in doc. curr."],
            invoice_id=row["Document Number"],
            profit_center=row["Profit Center"]
        )
        invoices.append(invoice)
    return invoices


# load closed invoices
def load_closed_invoices(filename="closed invoices.xlsx"):
    try:
        df = pd.read_excel(filename)
    except FileNotFoundError:
        print(f"File {filename} not found")
        return []
    invoices = []
    for _, row in df.iterrows():
        invoice = ClosedInvoice(
            status=row["Status"],
            customer_id=row["Payer Number"],
            customer_name=row["Customer Name"],
            co_code=row["Company Code"],
            invoice_date=row["Document Date"],
            due_date=row["Net due date"],
            document_currency=row["Document currency"],
            amount=row["Amount in doc. curr."],
            invoice_id=row["Document Number"],
            profit_center=row["Profit Center"],
            payment_date=row["Payment date"]
        )
        invoices.append(invoice)
    return invoices
