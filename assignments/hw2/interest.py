"""
Joseph Fagua
interest.py

Problem: Calculate the monthly interest charge on a credit card account.

Certificate of Authenticity: I certify that this assignment is entirely my work.
"""


def main():
    apr = eval(input("Enter annual interest rate:"))
    days_of_billing_cycle = eval(input("Enter the number of days in the billing cycle:"))
    previous_balance = eval(input("Enter the previous net balance:"))
    installment = eval(input("Enter the payment amount:"))
    payment_day = eval(input("Enter the day of billing cycle when payment was made:"))

    sum_of_net = previous_balance * days_of_billing_cycle
    days_before_end_of_cycle = days_of_billing_cycle - payment_day
    sum_of_remaining_days = installment * days_before_end_of_cycle
    average_monthly_balance = sum_of_net - sum_of_remaining_days
    average_daily_balance = average_monthly_balance / days_of_billing_cycle
    monthly_interest_charge = (average_daily_balance * (apr / 12)) / 100
    print(round(monthly_interest_charge, 2))


if __name__ == '__main__':
    main()
