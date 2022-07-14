class Node():
    def __init__(self,data, next = None):
        self.data = data
        self.next = next
    def getData(self):
        return self.data
    def setData (self,d):
        self.data = d
    def getNext (self):
        return self.next
    def setNext (self, n):
        self.next = n
    def __str__(self):
        return str(self.data) + " whose next node is " + str(self.next)