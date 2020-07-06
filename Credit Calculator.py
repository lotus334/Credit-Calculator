# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 08:27:41 2020

@author: OKS-8
"""
from math import log
from math import ceil
from math import floor

def mon_payment(principals, period):
    global payment
    if principals % period == 0:
        payment = int(principals / period)
        return f'Your monthly payment = {payment}'
    else:
        payment = int(round(principals / period, 0)) + 1
        global last_payment
        last_payment = principals - (period - 1) * payment
        return f'Your monthly payment = {payment} with last month payment = {last_payment}.'

def count_of_months():
    print('Enter the credit principal:')
    principals = int(input())
    print('Enter monthly payment:')
    mon_pay = int(input())
    print('Enter credit interest:')
    interest = float(input())
    nominal_interest = interest / (12 * 100)
    period = log((mon_pay / (mon_pay - nominal_interest * principals)),(1 + nominal_interest))
    rounded_period = ceil(period)
    years = rounded_period // 12
    months = rounded_period % 12
    if years == 0 and months == 1:
        print(f'You need {months} month to repay this credit')
    elif years == 1 and months == 1:
        print(f'You need {years} year and {months} month to repay this credit')
    elif years == 1 and months != 1:
        print(f'You need {years} year and {months} months to repay this credit')
    elif years != 0 and months == 1:
        print(f'You need {years} years and {months} month to repay this credit')
    elif years == 0 and months != 1:
        print(f'You need {months} months to repay this credit')
    elif years != 0 and months != 1:
        print(f'You need {years} years and {months} months to repay this credit!')

def annuity_monthly_payment():
    print('Enter credit principal:')
    principals = int(input())
    print('Enter count of periods:')
    period = int(input())
    print('Enter credit interest:')
    interest = float(input())
    nominal_interest = interest / (12 * 100)
    ordinary_annuity = ceil(principals * (nominal_interest * (1 + nominal_interest)**period) / ((1 + nominal_interest)**period - 1))
    print(f'Your annuity payment = {ordinary_annuity}!')

def credit_principal():
    print('Enter monthly payment:')
    ordinary_annuity = float(input())
    print('Enter count of periods:')
    period = int(input())
    print('Enter credit interest:')
    interest = float(input())
    nominal_interest = interest / (12 * 100)
    principals = ceil(ordinary_annuity / ((nominal_interest * (1 + nominal_interest)**period) / ((1 + nominal_interest)**period - 1)))-1
    print(f'Your credit principal = {principals}!')

def calculate():
    print('What do you want to calculate?')
    print('type "n" - for count of months,')
    print('type "a" - for annuity monthly payment,')
    print('type "p" - for credit principal:')
    action = input()
    if action == 'n':
        count_of_months()
    elif action == 'a':
        annuity_monthly_payment()
    elif action == 'p':
        credit_principal()
calculate()