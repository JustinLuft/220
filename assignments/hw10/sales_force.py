"""
sales_force.py
I certify that this code is written by me, Justin Luft
"""
from sales_person import SalesPerson
class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        infile = open(file_name, "r")
        slist = []
        for line in infile:
            line = line.split(",")
            saleperson = SalesPerson(int(line[0]), str(line[1]))
            slist = saleperson.get_id(), saleperson.get_name(), saleperson.get_sales()
            self.sales_people.append(slist)

    def quota_report(self, quota):
        qlist = []
        infile = open("salesData.txt", "r")
        for line in infile:
            line = line.split(",")
            saleperson = SalesPerson(int(line[0]), str(line[1]))
            if saleperson.met_quota(quota) == True:
                slist = saleperson.get_id(), saleperson.get_name(), saleperson.get_sales(), True
            else:
                slist = saleperson.get_id(), saleperson.get_name(), saleperson.get_sales(), False
            qlist.append(slist)
        return qlist

    def top_seller(self):
        tlist = []
        slist = []
        mlist = []
        infile = open("salesData.txt", "r")
        for line in infile:
            line = line.split(",")
            saleperson = SalesPerson(int(line[0]), str(line[1]))
            slist.append(str(line[1]))
            total = saleperson.total_sales()
            tlist.append(total)
        maxnum = max(tlist)
        acc = 0
        for i in tlist:
            if i == maxnum:
                mlist.append(slist[acc])
                acc = acc + 1
            else:
                acc = acc + 1
        return mlist
    def individual_sales(self, employee_id):
        infile = open("salesData.txt", "r")
        for line in infile:
            line = line.split(",")
            if str(line[0]) == str(employee_id):
                print(SalesPerson(line[0], line[1]))
                return SalesPerson(line[0], line[1])
        return None










