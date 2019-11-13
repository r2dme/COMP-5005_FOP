from accounts import BankAccount

def balances():
    print('\n#### Balances ####\n')
    total = 0
    for i in range(len(my_accounts)):
        print("Name: ", my_accounts[i].name, "\tNumber: ", my_accounts[i].number, \
              "\tBalance: ", my_accounts[i].balance)
        total = total + my_accounts[i].balance
    print("\t\t\t\t\tTotal: ", total)

savings = BankAccount('Savings','123456',3000)
cheque = BankAccount('Cheque','234567',300)



print('\n#### Bank Accounts ####\n')

my_accounts = []
account = BankAccount('Savings','123456',3000)
my_accounts.append(account)
account = BankAccount('Cheque','234567',300)
my_accounts.append(account)

balances()

my_accounts[0].deposit(100)
my_accounts[1].withdraw(30)
my_accounts[1].withdraw(1000)
my_accounts[0].add_interest()
my_accounts[1].add_interest()
my_accounts[0].apply_fees()
my_accounts[1].apply_fees()

balances()


