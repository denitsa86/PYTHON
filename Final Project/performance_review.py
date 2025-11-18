import pandas as pd
from openpyxl import load_workbook
from report_generator import sum_current_due_invoices

#def calculate_overall_performance():
    # total_to_be_collected would be sum of all open and closed invoices due from 1st day of the current
    # month until last day - 1
    #total_to_be_collected = ?
    #target is the overdue to be < 5%
    #allowed_overdue = total_to_be_collected * 0.05
    #if sum of def sum_current_due_invoices(open_invoices) > allowed_overdue calculate the % at the moment
    #this means what % is sum_current_due_invoices from total to be collected
    # print the result "Current overdue % is ... .If it`s below 5%- print Target reached, if it`s >= 5%
    #print Target not reached and calculate sum_current_due_invoices - allowed overdue to find out how
    #much has to be collected to reach the target

#def calculate_individual_performance - same but for each collector

