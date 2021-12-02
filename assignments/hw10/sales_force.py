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
        infile = open(file_name, "r")
        for line in infile:
            self.sales_people += line

    def quota_report(self, quota):
        pass

    def top_seller(self):
        top = []
        for i in range(len(self.sales_people)):
            highest = self.sales_people[i].get_sales()
            pos = i
            for j in range(i, len(self.sales_people)):
                if self.sales_people[j].get_sales() > highest:
                    highest = self.sales_people[j].get_sales()
                    pos = j
            self.sales_people[i], self.sales_people[pos] = self.sales_people[pos], self.sales_people[i]
        top.append(self.sales_people[0])
        for i in range(1, len(self.sales_people)):
            if self.sales_people[i].total_sales() == top[0].total_sales():
                top.append(self.sales_people[i])
        return top

    def individual_sales(self, employee_id):
        for person in self.sales_people:
            if person.get_id() == employee_id:
                return person
        return None
