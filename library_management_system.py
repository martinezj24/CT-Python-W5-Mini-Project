from library import add_book, borrow_book, return_book, search_book, display_all_books, add_user, view_user_details, display_all_users
from database import connect_to_database



def main():

    try:
        connection = connect_to_database()
        if connection is None:
            return

        while True:

            print('''
            Welcome to the Library Management System with Database Integration!
            **** 
            Main Menu:
            1. Book Operations
            2. User Operations
            3. Quit''')

            choice = input('Enter your choice: ')

            if choice == '1':
                book_operations(connection)
            elif choice == '2':
                user_operations(connection)
            elif choice == '3':
                print('Goodbye!')
                break
            else:
                print('Invalid choice! Please enter a valid option')
                
    except Error as e: #Dylan/Travis Proof
            print(f"Error: {e}")



def book_operations(connection):

    try:
        while True:

            print('''\nBook Operations:
            1. Add a new book
            2. Borrow a book
            3. Return a book
            4. Search for a book
            5. Display all books
            6. Back to Main Menu''')

            choice = input('Enter your choice: ')

            if choice == '1':
                title = input('Enter the title of the book: ')
                isbn = input('Enter the ISBN of the book: ')
                publication_date = input('Enter the publication date of the book (YYYY-MM-DD): ')
                availability = input('Is the book available? (Y/N): ')
                availability = True if availability.lower() == 'y' else False
                add_book(connection, title, isbn, publication_date, availability)
            elif choice == '2':
                user_id = int(input('Enter the user ID: '))
                book_id = int(input('Enter the book ID: '))
                borrow_book(connection, user_id, book_id)
            elif choice == '3':
                user_id = int(input('Enter the user ID: '))
                book_id = int(input('Enter the book ID: '))
                return_book(connection, user_id, book_id)
            elif choice == '4':
                title = input('Enter the title of the book to search: ')
                search_book(connection, title)
            elif choice == '5':
                display_all_books(connection)
            elif choice == '6':
                break
            else:
                print('Invalid choice! Please enter a valid option.')

    except Error as e: #Dylan/Travis Proof
        print(f"Error: {e}")




def user_operations(connection):

    try:
        while True:

            print('''\nUser Operations:
            1. Add a new user
            2. View user details
            3. Display all users
            4. Back to Main Menu''')

            choice = input('Enter your choice: ')

            if choice == '1':
                name = input('Enter the name of the user: ')
                email = input('Enter the email of the user: ')
                add_user(connection, name, email)
            elif choice == '2':
                search_criteria = input('Enter the name or email of the user to search: ')
                view_user_details(connection, search_criteria)
            elif choice == '3':
                display_all_users(connection)
            elif choice == '4':
                break
            else:
                print('Invalid choice! Please enter a valid option')

    except Error as e: #Dylan/Travis Proof
        print(f"Error: {e}")

main()
