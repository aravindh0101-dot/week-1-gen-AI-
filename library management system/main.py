books = []

while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Add Book
    if choice == "1":

        book_name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")

        book = {
            "book_name": book_name,
            "author": author,
            "issued": False
        }

        books.append(book)

        print("Book Added Successfully!")

    # View Books
    elif choice == "2":

        if len(books) == 0:

            print("No Books Available")

        else:

            print("\nBook Records")

            for book in books:

                print("----------------------")
                print("Book Name:", book["book_name"])
                print("Author:", book["author"])

                if book["issued"]:
                    print("Status: Issued")
                else:
                    print("Status: Available")

    # Search Book
    elif choice == "3":

        search_book = input("Enter Book Name to Search: ")

        found = False

        for book in books:

            if book["book_name"].lower() == search_book.lower():

                print("\nBook Found")
                print("Book Name:", book["book_name"])
                print("Author:", book["author"])

                if book["issued"]:
                    print("Status: Issued")
                else:
                    print("Status: Available")

                found = True

        if not found:
            print("Book Not Found")

    # Issue Book
    elif choice == "4":

        issue_book = input("Enter Book Name to Issue: ")

        found = False

        for book in books:

            if book["book_name"].lower() == issue_book.lower():

                if not book["issued"]:

                    book["issued"] = True

                    print("Book Issued Successfully")

                else:
                    print("Book Already Issued")

                found = True

        if not found:
            print("Book Not Found")

    # Return Book
    elif choice == "5":

        return_book = input("Enter Book Name to Return: ")

        found = False

        for book in books:

            if book["book_name"].lower() == return_book.lower():

                if book["issued"]:

                    book["issued"] = False

                    print("Book Returned Successfully")

                else:
                    print("Book Was Not Issued")

                found = True

        if not found:
            print("Book Not Found")

    # Delete Book
    elif choice == "6":

        delete_book = input("Enter Book Name to Delete: ")

        found = False

        for book in books:

            if book["book_name"].lower() == delete_book.lower():

                books.remove(book)

                print("Book Deleted Successfully")

                found = True
                break

        if not found:
            print("Book Not Found")

    # Exit
    elif choice == "7":

        print("Thank You!")

    else:
        print("Invalid Choice")