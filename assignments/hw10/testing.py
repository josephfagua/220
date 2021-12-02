from sales_person import SalesPerson
from sales_force import SalesForce


def main():
    employee = SalesPerson(124, "Charles Smith")
    employee.enter_sale(260.00)
    employee.enter_sale(140.00)
    employee.enter_sale(120.45)
    print(employee.__str__())


if __name__ == "__main__":
    main()
