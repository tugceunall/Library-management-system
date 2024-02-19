class Library:
    def __init__(self, file_name="books.txt"):
        self.file_name = file_name
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        print("Books available in the library:")
        for line in self.file:
            book_info = line.strip().split(",")
            print(f"Book: {book_info[0]}, Author: {book_info[1]}, Release Date: {book_info[2]}, Pages: {book_info[3]}")

    def add_book(self):
        book_name = input("Enter book title: ")
        author = input("Enter book author: ")
        release_date = input("Enter release date (YYYY-MM-DD): ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{book_name},{author},{release_date},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        book_title = input("Enter the title of the book to remove: ")
        lines = self.file.readlines()
        self.file.seek(0)
        self.file.truncate()
        for line in lines:
            if book_title not in line:
                self.file.write(line)
        print("Book removed successfully.")

# Creating an object named "lib" with "Library" class
lib = Library()

# Creating a menu to interact with the "lib" object
print("*** MENU ***")
print("1) List Books")
print("2) Add Book")
print("3) Remove Book")

menu_choice = input("Enter your choice: ")

if menu_choice == "1":
    lib.list_books()
elif menu_choice == "2":
    lib.add_book()
elif menu_choice == "3":
    lib.remove_book()
else:
    print("Invalid choice. Please select a valid option.")
