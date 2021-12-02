"""
Name: Joseph Fagua
sales_force.py
Purpose: Develop a class that creates a sales person object

Certification of Authenticity:
I certify that this work is entirely my own.
"""
from sales_person import SalesPerson


class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        file = open(file_name, "r")
        for line in file:
            self.sales_people += line

    def top_seller(self):
        pass

    def individual_sales(self, employee_id):
        pass