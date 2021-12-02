from sales_person import SalesPerson


def main():
    employee = SalesPerson(124, "Charles Smith")
    employee.enter_sale(200.00)
    employee.enter_sale(140.00)
    employee.enter_sale(120.45)
    print(employee.total_sales())
    print(employee.met_quota(450))
    print(employee.__str__)


if __name__ == "__main__":
    main()
