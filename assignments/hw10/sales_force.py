"""
sales_force.py
salesforce class
I certify that this code is written by me, Justin Luft
"""

from sales_person import SalesPerson
class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        infile = open(file_name, "r")
        for line in infile:
            line = line.split(",")
            line[1] = line[1][1:]
            saleperson = SalesPerson(int(line[0]), str(line[1]))
            listsell = line[2].split()
            for i in listsell:
                saleperson.enter_sale(float(i))

            self.sales_people.append(saleperson)

    def quota_report(self, quota):
        qlist = []
        for saleperson in self.sales_people:
            if saleperson.met_quota(quota):
                slist = saleperson.get_id(), saleperson.get_name(), saleperson.total_sales(), True
            else:
                slist = saleperson.get_id(), saleperson.get_name(), saleperson.total_sales(), False
            qlist.append(slist)
        return qlist

    def top_seller(self):
        tlist = []
        mlist = []
        for saleperson in self.sales_people:
            saleperson = str(saleperson)
            pt1 = saleperson.split(":")
            total = pt1[1]
            tlist.append(float(total))
        maxnum = max(tlist)
        acc = 0
        for i in tlist:
            if i == maxnum:
                mlist.append(self.sales_people[acc])
                acc = acc + 1
            else:
                acc = acc + 1
        return mlist
    def individual_sales(self, employee_id):
        acc = 0
        for saleperson in self.sales_people:
            saleperson = str(saleperson)
            pt1 = saleperson.split("-")
            pt2 = int(pt1[0])
            if pt2 == employee_id:
                return self.sales_people[acc]
            acc = acc + 1
        return None
