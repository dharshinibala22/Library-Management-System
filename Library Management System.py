books = []

def add_book():
    book_id = input("Book ID: ")
    title = input("Book Title: ")
    author = input("Author Name: ")
    copies = int(input("Number of Copies: "))

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "copies": copies,
        "available": copies
    }
    books.append(book)
    print("Book Added Successfully!\n")

def show_books():
    if len(books) == 0:
        print("No books in library yet.\n")
        return

    print("\n---- Library Books ----")
    for book in books:
        print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Available: {book['available']}/{book['copies']}")
    print("")

def find_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None

def issue_book():
    book_id = input("Enter Book ID to issue: ")
    book = find_book(book_id)

    if book is None:
        print("Book not found!\n")
    elif book["available"] == 0:
        print("Sorry, no copies available right now.\n")
    else:
        book["available"] -= 1
        print(f"Book '{book['title']}' issued successfully!\n")

def return_book():
    book_id = input("Enter Book ID to return: ")
    book = find_book(book_id)

    if book is None:
        print("Book not found!\n")
    elif book["available"] == book["copies"]:
        print("All copies are already in library.\n")
    else:
        book["available"] += 1
        print(f"Book '{book['title']}' returned successfully!\n")

def search_book():
    keyword = input("Enter title or author to search: ").lower()
    found = False

    for book in books:
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Available: {book['available']}/{book['copies']}")
            found = True

    if not found:
        print("No matching books found.\n")

def main():
    while True:
        print("===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Show All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            show_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print("Thank you! Exiting program...")
            break
        else:
            print("Invalid choice, please try again.\n")

main()
