# class Person:
#     pid = 100
#
#     def __init__(self, fname, lname):
#         Person.pid += 1
#         self.id = Person.pid
#         self.firstname = fname
#         self.lastname = lname
#
#     def __str__(self):
#         return "%d %s %s" % (self.id, self.firstname, self.lastname)
#
#
# def runsomething():
#     p1 = Person('Joe', 'Blow')
#     print(p1)
#     p1 = Person('Jill', 'Blow')
#     print(p1)
#
# if __name__ == '__main__':
#     runsomething()
#
#
#
#     class Account:
#         aid = 100
#
#         def __init__(self, atype, aowner):
#             Account.aid += 1
#             self.id = Account.aid
#             self.type = atype
#             self.owner = aowner
#             self.balance = 0.0
#
#
#         def __str__(self):
#             return "Acct %d %s Owner %s Balance %f" % (self.id, self.type, self.owner, self.balance)
#
#         def getid(self):
#             return self.id
#
#
# def PRINT():
#     pass
#
#
# class Bank():
#     def __init__(self):
#         self.customers = {}
#         self.accounts = {}
#
#     def add_customer(self, cust):
#         cid = cust.getid()
#         if cid in self.customers:
#             print("Customer already exists")
#         else:
#             self.customers[cid] = cust
#
#     def add_account(self, acct):
#         pass
#
#     def remove_account(self, acct):
#         pass
#
#     def deposit(self, amt):
#         pass
#
#     def withdrawal(self, amt):
#         pass
#
#     def balance_inquiry(self, acct):
#                 #PRINT('${:,.2f}'.')
#
#     def __str__(self):
#         return self.stringCustomers()
#
#     def printCustomers(self):
#         print(self.customers)
#
#         def runsomething():
#             p1 = Person('Joe', 'Blow')
#             print(p1)
#             p2 = Person('Jill', 'Blow')
#             print(p1)
#             a1 = Account("SAVINGS", p1)
#             a2 = Account("CHECKING", p2)
#
#             zc_bank = Bank()
#             bob = Person("Bob", "Smith")
#             zc_bank.add_customer(bob)
#
#             zc_bank.printCustomers()
#             print(a2)
#
#
#
#
#         if __name__ == '__main__':
#             runsomething()