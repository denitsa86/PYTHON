import pandas as pd
from customer import Customer
from collector import Collector
from account_manager import AccountManager
from invoice import Invoice

def load_customers(filename="customers.xlsx"):
    df = pd.read_excel(filename)
    return [Customer(row["PayerNumber"], row["CustomerName"]) for _, row in df.iterrows()]

def load_collectors(filename="collectors.xlsx"):
    df = pd.read_excel(filename)
    return [Collector(row["CollectorName"], row["CollectorManager"]) for _, row in df.iterrows()]

def load_account_managers(filename="account_managers.xlsx"):
    df = pd.read_excel(filename)
    return [AccountManager(row["ManagerName"], row["Business"], row["ManagedPayer"]) for _, row in df.iterrows()]

def load_open_invoices(filename="open invoices.xlsx"):
    df = pd.read_excel(filename)
    return [
        Invoice(
            row["InvoiceID"],
            row["CustomerID"],
            row["CustomerName"],
            row["InvoiceDate"],
            row["DueDate"],
            row["AmountDocCurrency"],
            row["DocCurrency"],
            row["Status"],
            row["CoCode"],
            row["ProfitCenter"],
        )
        for _, row in df.iterrows()
    ]
def load_closed_invoices(filename="closed invoices.xlsx"):
    df = pd.read_excel(filename)
    return [
        Invoice(
            row["InvoiceID"],
            row["CustomerID"],
            row["CustomerName"],
            row["InvoiceDate"],
            row["DueDate"],
            row["AmountDocCurrency"],
            row["DocCurrency"],
            row["Status"],
            row["CoCode"],
            row["ProfitCenter"],
        )
        for _, row in df.iterrows()
    ]

def convert_to_USD(input_file="open invoices.xlsx", output_file="open invoices converted.xlsx"):
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