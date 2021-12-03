"""
Name: Joseph Fagua
sales_person.py
Purpose: Develop a class that creates a sales person object

Certification of Authenticity:
I certify that this work is entirely my own.
"""


class SalesPerson:
    """encapsulates data for a sales person"""

    def __init__(self, employee_id, name):
        """constructs the class instance variables"""
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        """returns the sales person's employee_id"""
        return self.employee_id

    def get_name(self):
        """returns the sales person's name"""
        return self.name

    def set_name(self, name):
        """sets the sales person's name"""
        self.name = name

    def enter_sale(self, sale):
        """adds the value of sale to the sales list"""
        sale = float(sale)
        self.sales.append(sale)

    def total_sales(self):
        """returns the sum of the sales person's sales"""
        acc = 0
        for sale in self.sales:
            acc += sale
        return float(acc)

    def get_sales(self):
        """returns the list of sales"""
        return self.sales

    def met_quota(self, quota):
        """returns bool if total sales meet or exceed quota or fail to"""
        if self.total_sales() >= quota:
            return True
        return False

    def compare_to(self, other):
        """compares self to other and returns -1, returns 1 or 0"""
        if other.total_sales() > self.total_sales():
            return -1
        if other.total_sales() < self.total_sales():
            return 1
        return 0

    def __str__(self):
        """returns "employee_id name: total sales" """
        return "{0}-{1}:{2}".format(str(self.employee_id), str(self.name), str(self.total_sales()))
