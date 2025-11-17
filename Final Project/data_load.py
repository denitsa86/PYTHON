import pandas as pd
from customer import Customer
from collector import Collector
from account_manager import AccountManager
from invoice import OpenInvoice
from invoice import ClosedInvoice
from datetime import datetime

def load_customers(filename="customers.xlsx"):
    df = pd.read_excel(filename)
    return [Customer(row["Payer number"], row["Customer Name"]) for _, row in df.iterrows()]

def load_collectors(filename="collectors.xlsx"):
    df = pd.read_excel(filename)
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

def load_account_managers(filename="account_managers.xlsx"):
    df = pd.read_excel(filename)
    return [AccountManager(row["Account Manager"], row["Business segment"], row["Managed Payer"]) for _, row in df.iterrows()]

def load_open_invoices(filename="open invoices.xlsx"):
    df = pd.read_excel(filename)
    invoices = []
    for _, row in df.iterrows():
        invoice = OpenInvoice(
            status = row["Status"],
            customer_id=row["Payer number"],
            customer_name=row["Customer Name"],
            co_code = row["Company Code"],
            invoice_date = row["Document Date"],
            due_date = row["Net due date"],
            document_currency=row["Document currency"],
            amount = row["Amount in doc. curr."],
            invoice_id=row["Document Number"],
            profit_center = row["Profit Center"]
        )
        invoices.append(invoice)
    return invoices

def load_closed_invoices(filename="closed invoices.xlsx"):
    df = pd.read_excel(filename)
    invoices = []
    for _, row in df.iterrows():
        invoice = ClosedInvoice(
            status=row["Status"],
            customer_id=row["Payer number"],
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

def convert_to_usd(input_file="open invoices.xlsx", output_file="open invoices converted.xlsx"):
    # Exchange rates
    rates = {"USD": 1.00, "EUR": 1.16, "GBP": 1.32, "TRY": 0.024, "PLN":0.27, "DKK": 0.16}

    # Load the file
    df = pd.read_excel(input_file)

    # Convert amounts
    df["Amount in USD"] = df["Amount in doc. curr."] * df["Document currency"].map(rates)

    # Save the updated file
    df.to_excel(output_file, index=False)
    print(f"Saved converted invoices to {output_file}")

    #THINK ABOUT OTHER CURRENCIES!!!

def calculate_days_late(input_file="open invoices.xlsx", output_file="open invoices converted2.xlsx"):
    # Load your invoices
    df = pd.read_excel(input_file)

    # Ensure due_date is a proper date
    df["Net due date"] = pd.to_datetime(df["Net due date"]).dt.date

    # Calculate days late
    today = datetime.today().date()
    df["Days Late"] = (today - df["Net due date"]).apply(lambda x: x.days)

    # Save back to Excel
    df.to_excel(output_file, index=False)
    print("Saved with days_late column")