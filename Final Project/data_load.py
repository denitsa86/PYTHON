import pandas as pd
from customer import Customer
from collector import Collector
from account_manager import AccountManager
from invoice import OpenInvoice
from invoice import ClosedInvoice

def load_customers(filename="customers.xlsx"):
    df = pd.read_excel(filename)
    return [Customer(row["Payer number"], row["Customer Name"]) for _, row in df.iterrows()]

def load_collectors(filename="collectors.xlsx"):
    df = pd.read_excel(filename)
    return [Collector(row["Collector Full Name"], row["Manager"]) for _, row in df.iterrows()]

def load_account_managers(filename="account_managers.xlsx"):
    df = pd.read_excel(filename)
    return [AccountManager(row["Account Manager"], row["Business segment"], row["Managed Payer"]) for _, row in df.iterrows()]

def load_open_invoices(filename="open invoices.xlsx"):
    df = pd.read_excel(filename)
    return [
        OpenInvoice(
            row["Document Number"],
            row["Payer Number"],
            row["Customer Name"],
            row["Document Date"],
            row["Net due date"],
            row["Amount in doc. curr."],
            row["Document currency"],
            row["Status"],
            row["Company Code"],
            row["Profit Center"],
        )
        for _, row in df.iterrows()
    ]
def load_closed_invoices(filename="closed invoices.xlsx"):
    df = pd.read_excel(filename)
    return [
        ClosedInvoice(
            row["Document Number"],
            row["Payer Number"],
            row["Customer Name"],
            row["Document Date"],
            row["Net due date"],
            row["Amount in doc. curr."],
            row["Document currency"],
            row["Status"],
            row["Company Code"],
            row["Profit Center"],
            row["Payment date"],
        )
        for _, row in df.iterrows()
    ]

def convert_to_usd(input_file="open invoices.xlsx", output_file="open invoices converted.xlsx"):
    # Exchange rates
    rates = {"USD": 1.00, "EUR": 1.16, "GBP": 1.32, "TRY": 0.024, "PLN":0.27, "DKK": 0.16}

    # Load the file
    df = pd.read_excel(input_file)

    # Convert amounts
    df["Amount in USD"] = df["AmountDocCurrency"] * df["DocCurrency"].map(rates)

    # Save the updated file
    df.to_excel(output_file, index=False)
    print(f"Saved converted invoices to {output_file}")

    #THINK ABOUT OTHER CURRENCIES!!!