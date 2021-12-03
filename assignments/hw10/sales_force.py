"""
Name: Joseph Fagua
sales_force.py
Purpose: Develop a class that creates a sales person object

Certification of Authenticity:
I certify that this work is entirely my own.
"""
from sales_person import SalesPerson


class SalesForce:
    """encapsulates data for a sales person"""
    def __init__(self):
        """ initializes sales_people to an empty list"""
        self.sales_people = []

    def add_data(self, file_name):
        """imports information for all salespeople from the specified file"""
        with open(file_name, "r") as file:
            for line in file.readlines():
                employee_id, name, employee_sales = line.split(", ")
                sales = employee_sales.split(" ")
                sales_person = SalesPerson(employee_id, name)
                for sale in sales:
                    sales_person.enter_sale(sale)
                self.sales_people.append(sales_person)

    def quota_report(self, quota):
        """returns a list of seller’s employee_id, name, total sales, and a boolean value"""
        people = []
        for per in self.sales_people:
            people.append([per.get_id(), per.get_name(), per.total_sales(), per.met_quota(quota)])
        return people

    def top_seller(self):
        """returns a list of SalesPerson objects with the highest sales amount"""
        top = []
        for i in range(len(self.sales_people)):
            highest = self.sales_people[i].get_sales()
            pos = i
            for j in range(i, len(self.sales_people)):
                if self.sales_people[j].get_sales() > highest:
                    highest = self.sales_people[j].get_sales()
                    pos = j
            self.sales_people[i],self.sales_people[pos]=self.sales_people[pos],self.sales_people[i]
        top.append(self.sales_people[0])
        for i in range(1, len(self.sales_people)):
            if self.sales_people[i].total_sales() == top[0].total_sales():
                top.append(self.sales_people[i])
        return top

    def individual_sales(self, employee_id):
        """returns the SalesPerson with the given employee_id or None if the id does not exist"""
        for person in self.sales_people:
            if person.get_id() == employee_id:
                return person
        return None
