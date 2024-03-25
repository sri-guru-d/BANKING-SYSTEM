from entity.model import Customer,Account,Transaction
from dao.bank_service_provider_impl import BankServiceProviderImpl
from exceptions.custom_exceptions import InsufficientBalanceException,InvalidAccountTypeException
from dao.ibank_service_provider import IBankServiceProvider,ICustomerServiceProvider

class BankApp:
    @staticmethod
    def main():
        bank_service = BankServiceProviderImpl()
        while True:
            print("\nMenu:")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Get Balance")
            print("6. Get Account Details")
            print("7. List Accounts")
            print("8. Get Transactions")
            print("9. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("\nCreating Account:")
                acc_type = input("Enter Account Type (Savings/Current/ZeroBalance): ")
                balance = float(input("Enter Initial Balance: "))
                customer_id = input("Enter Customer ID: ")  # Assuming customer already exists
                customer = Customer(customer_id, "John Doe", "john@example.com", "1234567890", "123 Main St", 700)  # Sample customer
                if bank_service.create_account(customer, acc_type, balance):
                    print("Account created successfully.")
                else:
                    print("Failed to create account.")

            elif choice == "2":
                print("\nDeposit:")
                account_number = int(input("Enter Account Number: "))
                amount = float(input("Enter Amount to Deposit: "))
                new_balance = bank_service.deposit(account_number, amount)
                if new_balance is not None:
                    print(f"Amount {amount} deposited successfully. New balance: {new_balance}")
                else:
                    print("Deposit failed. Please check account number.")

            elif choice == "3":
                print("\nWithdraw:")
                account_number = int(input("Enter Account Number: "))
                amount = float(input("Enter Amount to Withdraw: "))
                try:
                    new_balance = bank_service.withdraw(account_number, amount)
                    print(f"Amount {amount} withdrawn successfully. New balance: {new_balance}")
                except InsufficientBalanceException as e:
                    print(f"Withdrawal failed: {e}")

            elif choice == "4":
                print("\nTransfer:")
                from_account_number = int(input("Enter From Account Number: "))
                to_account_number = int(input("Enter To Account Number: "))
                amount = float(input("Enter Amount to Transfer: "))
                try:
                    new_balance = bank_service.transfer(from_account_number, to_account_number, amount)
                    print(f"Amount {amount} transferred successfully. New balance: {new_balance}")
                except InsufficientBalanceException as e:
                    print(f"Transfer failed: {e}")

            elif choice == "5":
                print("\nGet Balance:")
                account_number = int(input("Enter Account Number: "))
                balance = bank_service.get_account_balance(account_number)
                if balance is not None:
                    print(f"Current balance of account {account_number}: {balance}")
                else:
                    print("Account not found.")

            elif choice == "6":
                print("\nGet Account Details:")
                account_number = int(input("Enter Account Number: "))
                account_details = bank_service.get_account_details(account_number)
                if account_details:
                    print(account_details)
                else:
                    print("Account not found.")

            elif choice == "7":
                print("\nList Accounts:")
                accounts = bank_service.list_accounts()
                if accounts:
                    for account in accounts:
                        print(account)
                        print("---------------------------------------------------------------")
                else:
                    print("No accounts found.")

            elif choice == "8":
                print("\nGet Transactions:")
                account_number = int(input("Enter Account Number: "))
                from_date = input("Enter From Date (YYYY-MM-DD): ")
                to_date = input("Enter To Date (YYYY-MM-DD): ")
                transactions = bank_service.get_transactions(account_number, from_date, to_date)
                if transactions:
                    for transaction in transactions:
                        print(transaction)
                else:
                    print("No transactions found.")

            elif choice == "9":
                print("Exiting Bank Application.")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    BankApp.main()