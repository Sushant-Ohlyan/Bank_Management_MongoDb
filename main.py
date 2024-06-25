# main.py

from account_manager import add_account, list_accounts, update_account, delete_account
from mongodb_utils import close_connection  # Import close_connection function


def main():
    try:
        while True:
            print("\n Bank Management App")
            print("1. List all accounts")
            print("2. Add a new account")
            print("3. Update an account")
            print("4. Delete an account")
            print("5. Exit the app")
            choice = input("Enter your choice: ")

            if choice == '1':
                list_accounts()
            elif choice == '2':
                name = input("Enter the account holder's name: ")
                balance = input("Enter the initial balance: $")
                add_account(name, balance)
            elif choice == '3':
                account_id = input("Enter the account ID to update: ")
                name = input("Enter the updated account holder's name: ")
                balance = input("Enter the updated balance: $")
                update_account(account_id, name, balance)
            elif choice == '4':
                account_id = input("Enter the account ID to delete: ")
                delete_account(account_id)
            elif choice == '5':
                break
            else:
                print("Invalid choice")

    finally:
        close_connection()  # Close MongoDB connection when exiting


if __name__ == "__main__":
    main()
