import pyodbc
from dao.ibank_service_provider import IBankServiceProvider
from dao.customer_service_provider_impl import CustomerServiceProviderImpl
from entity.model import Account
from util.db_conn_util import DBUtil


class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class to initialize the 'accounts' attribute
        self.conn = DBUtil.get_db_conn()    

    def create_account(self, customer, acc_type, balance):
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO Accounts (customer_id, account_type, balance) VALUES (?, ?, ?)",
                           (customer.customer_id, acc_type, balance))
            self.conn.commit()
            return True
        except pyodbc.Error as ex:
            print(f"Error creating account: {ex}")
            return False
        finally:
            cursor.close()

    def list_accounts(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT * FROM Accounts")
            accounts = []
            for row in cursor.fetchall():
                # Assuming the row structure matches the Account class attributes
                account = Account(row[1], row[2], row[3])  # Modify as per your database schema
                accounts.append(account)
            return accounts
        except pyodbc.Error as ex:
            print(f"Error listing accounts: {ex}")
            return None
        finally:
            cursor.close()
