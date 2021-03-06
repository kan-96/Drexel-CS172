class Employee():
    count_attr = 1

    def __init__(self, name, rate=0.0):
        self.name = name
        self.eid = Employee.count_attr
        self.hours = 0.0
        self.rate = rate
        Employee.count_attr += 1

    def getRate(self):
        return float(self.rate)

    def setRate(self, r):
        self.rate = r

    def getEID(self):
        return self.eid

    def getHours(self):
        return float(self.hours)

    def setHours(self, h):
        self.hours = h

    def getGrossPay(self):
        pay = float(self.rate) * float(self.hours)
        return pay

    def __eq__(self, ID):
        match = int(self.eid) == int(ID)
        return match
    def __str__(self):
        s = ''
        s += 'Employee Name: ' + self.name
        s += "\nEmployee ID: " + str(self.eid)
        s += ('\nHourly Rate: {}'.format(float(self.rate)))
        s += "\nHours Worked: {}".format(float(self.hours))
        s += "\nGross Pay: {}".format(float(self.getGrossPay()))
        s += "\n"
        return s