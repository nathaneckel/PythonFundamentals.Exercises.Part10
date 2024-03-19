#DONE - Paste Kris' code in here
#DONE - Pickle the code

# small_town_teller.py
import pickle



# Declare a Person class with the following attributes:
#
# id
# first name
# last name
class Person:
    pid = 100

    def __init__(self, fname, lname):
        Person.pid += 1
        self.id = Person.pid
        self.firstname = fname
        self.lastname = lname

    def __str__(self):
        return "(%d) %s %s" % (self.id, self.firstname, self.lastname)

    def getid(self):
        return self.id

# Declare an Account class with the following attributes:
# number
# type
# owner
# balance
class Account():
    aid = 100

    def __init__(self, atype, aowner):
        Account.aid += 1
        self.id = Account.aid
        self.type = atype
        self.owner = aowner
        self.balance = 0.0

    def __str__(self):
        return "Acct %d: %s Owner: %s  Balance: %f" % (self.id, self.type, self.owner, self.balance)

    def getid(self):
        return self.id

class Bank():

    def __init__(self):
        self.customers = {}
        self.accounts = {}


    def add_customer(self, cust):
        cid = cust.getid()
        if cid in self.customers:
            raise Exception("Customer already exists")
        else:
            self.customers[cid] = cust

    def add_account(self, acct):
        aid = acct.getid()
        if aid in self.accounts:
            raise Exception("Account already exists")
        else:
            self.accounts[aid] = acct

    def remove_account(self, acct):
        del self.accounts[acct.getid()]

    def deposit(self, acctid, amt):
        # acct.balance = acct.balance + amt
        self.accounts[acctid].balance = self.accounts[acctid].balance + amt

    def withdrawal(self, acctid, amt):
        # if balance < amt then exception (you aint got that much money))
        self.accounts[acctid].balance = self.accounts[acctid].balance - amt

    def balance_inquiry(self, acctid):
        #   '${:,.2f}'.format(1234.5)
        print('${:,.2f}'.format(self.accounts[acctid].balance))

    def __str__(self):
        return str(self.accounts) + str(self.customers)

    def printCustomers(self):
        print("Customers:")
        for c in self.customers.items():
            print(c[1])

    def printAccounts(self):
        print("Accounts:")
        for c in self.accounts.items():
            print(c[1])


def runsomething():
    p1 = Person('Joe', 'Blow')
    # print(p1)
    p2 = Person('Jill', 'Blow')
    # print(p2)
    a1 = Account("SAVINGS", p1)
    a2 = Account("CHECKING", p2)

    zc_bank = Bank()
    bob = Person("Bob", "Smith")
    zc_bank.add_customer(bob)

    zc_bank.printCustomers()

    bob_savings = Account("SAVINGS", bob)
    zc_bank.add_account(bob_savings)

    zc_bank.printAccounts()

    zc_bank.balance_inquiry(bob_savings.getid())
    # 0
    zc_bank.deposit(bob_savings.getid(), 256.02)
    zc_bank.balance_inquiry(bob_savings.getid())
    # 256.02
    zc_bank.withdrawal(bob_savings.getid(), 128)
    zc_bank.balance_inquiry(bob_savings.getid())
    # 128.02

if __name__ == '__main__':

    # with open('KrisBank.pickle', 'rb') as handle:
    #     zc_bank = pickle.load(handle)

        runsomething()

        # with open('KrisBank.pickle', 'wb') as handle:
        #     pickle.dump(zc_bank, handle, protocol=pickle.HIGHEST_PROTOCOL)

#
# zc_bank = Bank()
# bob = Person("Bob", "Smith")
# zc_bank.add_customer(bob)
#
# with open('KrisBank.pickle', 'wb') as handle:
#     pickle.dump(zc_bank, handle, protocol=pickle.HIGHEST_PROTOCOL)
#
# with open('filename.pickle', 'rb') as handle:
#     zc_bank2 = pickle.load(handle)
#     print(zc_bank, zc_bank2)