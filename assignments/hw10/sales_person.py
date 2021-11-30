"""
sales_person.py
SalesPerson class
I certify that this code is written by me, Justin Luft
"""

class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        acc = 0
        sales = self.sales
        for i in self.sales:
            acc = acc + i
        return float(acc)

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        total = 0
        for i in self.sales:
            total = total + i
        print(total)
        if total >= quota:
            return True
        else:
            return False

    def compare_to(self, other):
        total = 0
        for i in self.sales:
            total = total + i
        salesy = other.total_sales()
        if salesy > total:
            return -1
        elif total > salesy:
            return 1
        elif total == salesy:
            return 0

    def __str__(self):
        total = 0
        for i in self.sales:
            total = total + i
        returnme = str(self.employee_id) + "-" + str(self.name) + ":" + str(total)
        return returnme
