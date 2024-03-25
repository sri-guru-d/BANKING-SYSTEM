import datetime
import pyodbc
from entity.model import Account
from exceptions.custom_exceptions import InsufficientBalanceException
from dao.ibank_service_provider import ICustomerServiceProvider

class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self):
        self.accounts = []

    def get_account_balance(self, account_number):
        cursor = self.conn.cursor()
        try:
                cursor.execute("SELECT balance FROM Accounts WHERE account_number = ?", (account_number,))
                row = cursor.fetchone()
                if row:
                    return row[0]
                else:
                    return None  # Account not found
        except pyodbc.Error as ex:
                print(f"Error retrieving account balance: {ex}")
                return None
        finally:
             cursor.close()


    def deposit(self, account_number, amount):
        cursor = self.conn.cursor()
        try:
        # Fetch the current balance of the account
            cursor.execute("SELECT balance FROM Accounts WHERE account_number = ?", (account_number,))
            row = cursor.fetchone()
            if row:
                balance = row[0]
                new_balance = balance + amount

            # Update the account balance
                cursor.execute("UPDATE Accounts SET balance = ? WHERE account_number = ?", (new_balance, account_number))

            # Insert transaction details into the transactions table
                cursor.execute("INSERT INTO transactions (account_number, transaction_type, amount, transaction_date) VALUES (?, ?, ?, ?)",
                           (account_number, 'deposit', amount, datetime.datetime.now()))

            # Commit the transaction
                self.conn.commit()
                return new_balance
            else:
                return None  # Account not found
        except pyodbc.Error as ex:
            print(f"Error depositing amount: {ex}")
            return None
        finally:
            cursor.close()


    def withdraw(self, account_number, amount):
        cursor = self.conn.cursor()
        try:
        # Fetch the current balance of the account
            cursor.execute("SELECT balance FROM Accounts WHERE account_number = ?", (account_number,))
            row = cursor.fetchone()
            if row:
                balance = row[0]
                if balance >= amount:
                    new_balance = balance - amount

                # Update the account balance
                    cursor.execute("UPDATE Accounts SET balance = ? WHERE account_number = ?", (new_balance, account_number))

                # Insert transaction details into the transactions table
                    cursor.execute("INSERT INTO transactions (account_number, transaction_type, amount, transaction_date) VALUES (?, ?, ?, ?)",
                               (account_number, 'withdraw', amount, datetime.datetime.now()))

                # Commit the transaction
                    self.conn.commit()
                    return new_balance
                else:
                    raise InsufficientBalanceException("Withdrawal exceeds available balance.")
            else:
                return None  # Account not found
        except pyodbc.Error as ex:
            print(f"Error withdrawing amount: {ex}")
            return None
        finally:
            cursor.close()


    def transfer(self, from_account_number, to_account_number, amount):
        cursor = self.conn.cursor()
        try:
        # Fetch balances of both accounts
            cursor.execute("SELECT balance FROM Accounts WHERE account_number = ?", (from_account_number,))
            from_balance = cursor.fetchone()[0]
            cursor.execute("SELECT balance FROM Accounts WHERE account_number = ?", (to_account_number,))
            to_balance = cursor.fetchone()[0]

        # Check if source account has sufficient balance
            if from_balance >= amount:
            # Deduct amount from source account and add to destination account
                from_new_balance = from_balance - amount
                to_new_balance = to_balance + amount

            # Update balances in the database
                cursor.execute("UPDATE Accounts SET balance = ? WHERE account_number = ?", (from_new_balance, from_account_number))
                cursor.execute("UPDATE Accounts SET balance = ? WHERE account_number = ?", (to_new_balance, to_account_number))
                self.conn.commit()

                return from_new_balance
            else:
                raise InsufficientBalanceException("Withdrawal exceeds available balance.")

        except pyodbc.Error as ex:
            print(f"Error transferring amount: {ex}")
            return None
        finally:
            cursor.close()


    def get_account_details(self, account_number):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT * FROM Accounts WHERE account_number = ?", (account_number,))
            row = cursor.fetchone()
            if row:
                # Assuming the row structure matches the Account class attributes
                account = Account(row[1], row[2], row[3])  # Modify as per your database schema
                return account
            else:
                return None  # Account not found
        except pyodbc.Error as ex:
            print(f"Error retrieving account details: {ex}")
            return None
        finally:
            cursor.close()

    def get_transactions(self, account_number, from_date, to_date):
        cursor = self.conn.cursor()
        try:
        # Fetch transactions between the specified dates for the given account
            cursor.execute("SELECT transaction_id, transaction_type, amount, transaction_date FROM Transactions WHERE account_number = ? AND transaction_date BETWEEN ? AND ?",
                       (account_number, from_date, to_date))
            transactions = cursor.fetchall()
            return transactions
        except pyodbc.Error as ex:
            print(f"Error fetching transactions: {ex}")
            return None
        finally:
            cursor.close()