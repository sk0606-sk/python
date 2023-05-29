class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.account_no} 已存款 {amount} 元")

    def withdraw(self, amount):
        if self.balance < amount:
            print("余额不足，无法取出")
        else:
            self.balance -= amount
            print(f"{self.account_no} 已取出 {amount} 元")


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"新账户 {account.account_no} 已创建")

    def display_accounts(self):
        for account in self.accounts:
            print(f"账户编号：{account.account_no},余额：{account.balance}")

    def search_account(self, account_no):
        for account in self.accounts:
            if account.account_no == account_no:
                return account
        return None


if __name__ == '__main__':
    b = Bank()
    b.add_account(BankAccount("123456", 0))  # 创建账户123456,初始余额为0元
    b.add_account(BankAccount("789012", 5000))  # 创建账户789012,初始余额为5000元
    b.display_accounts()  # 显示所有账户信息
    b.withdraw(2000)  # 从账户123456中取出2000元
    b.display_accounts()  # 显示所有账户信息
    b.search_account("789012")  # 在所有账户中搜索账户789012,返回该账户对象
