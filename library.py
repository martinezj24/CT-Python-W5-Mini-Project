from database import connect_to_database, execute_query, fetch_all



def add_book(connection, title, isbn, publication_date, availability=True):
    try:
        query = "INSERT INTO books (title, isbn, publication_date, availability) VALUES (%s, %s, %s, %s)"
        data = (title, isbn, publication_date, availability)
        if execute_query(connection, query, data):
            print('New book added successfully!')
        else:
            print('Failed to add the book')

    except Error as e: #Dylan/Travis Proof
            print(f"Error: {e}")



def borrow_book(connection, user_id, book_id):
    try:

        query = "UPDATE books SET availability = 0 WHERE id = %s"
        data = (book_id,)
        if execute_query(connection, query, data):
            query = "INSERT INTO borrowed_books (user_id, book_id) VALUES (%s, %s)"
            data = (user_id, book_id)
            if execute_query(connection, query, data):
                print('Book borrowed successfully!')
            else:
                print('Failed to borrow the book')
        else:
            print('Failed to borrow the book')

    except Error as e: #Dylan/Travis Proof
            print(f"Error: {e}")



def return_book(connection, user_id, book_id):
    try:
        query = "UPDATE books SET availability = 1 WHERE id = %s"
        data = (book_id,)
        if execute_query(connection, query, data):
            query = "UPDATE borrowed_books SET return_date = CURRENT_DATE WHERE user_id = %s AND book_id = %s"
            data = (user_id, book_id)
            if execute_query(connection, query, data):
                print('Book Returned Successfully!')
            else:
                print(f'Failed to Return Book ID: {book_id}')
        else:
            print(f'Failed to Return Book ID: {book_id}')
    except Error as e: #Dylan/Travis Proof
            print(f"Error: {e}")



def search_book(connection, title):
    try:

        query = "SELECT * FROM books WHERE title LIKE %s"
        data = (f"%{title}%",) 
        results = fetch_all(connection, query, data)
        if results:
            for result in results:
                print('Book Found!')
                print(result)
        else:
            print(f"No Books Found With Title: {title}")
    except Error as e: #Dylan/Travis Proof
            print(f"Error: {e}")


def display_all_books(connection):
    try:

        query = "SELECT * FROM books"
        results = fetch_all(connection, query)
        if results:
            for result in results:
                print('All Books In Library:')
                print(result)
        else:
            print('No books found.')
    except Error as e: #Dylan/Travis Proof
            print(f"Error: {e}")



def add_user(connection, name, email):
    try:

        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        data = (name, email)
        if execute_query(connection, query, data):
            print('New user added successfully!')
        else:
            print('Failed to add the user')
    except Error as e: #Dylan/Travis Proof
            print(f"Error: {e}")



def view_user_details(connection, search_criteria):

    try:
        query = "SELECT * FROM users WHERE name LIKE %s OR email LIKE %s"
        data = (f"%{search_criteria}%", f"%{search_criteria}%")
        results = fetch_all(connection, query, data)
        if results:
            for result in results:
                print(result)
        else:
            print(f"No users found with this search criteria: {search_criteria}")
    except Error as e: #Dylan/Travis Proof
            print(f"Error: {e}")


def display_all_users(connection):
    try:
        query = "SELECT * FROM users"
        results = fetch_all(connection, query)
        if results:
            for result in results:
                print('All Users: ')
                print(result)
        else:
            print('No users found')
    except Error as e: #Dylan/Travis Proof
            print(f"Error: {e}")
