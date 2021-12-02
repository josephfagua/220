"""
Name: Joseph Fagua
sales_person.py
Purpose: Develop a class that creates a sales person object

Certification of Authenticity:
I certify that this work is entirely my own.
"""


class SalesPerson:
    def __init__(self, employee_id, name):
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
        sale = round(float(sale), 2)
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
        """compares self to other and returns -1 if other has more in total sales than self, returns 1 if self has more
        in total sales than other, and 0 if their total sales are the same """
        if other.total_sales() > self.total_sales():
            return -1
        elif other.total_sales() < self.total_sales():
            return 1
        elif other.total_sales() == self.total_sales():
            return 0

    def __str__(self):
        """returns "<employee_id><name>: <total sales>" """
        return self.employee_id, self.name, self.total_sales()
