class Library:
    def __init__(self):

        self.books = []

        print("Welcome to the Python Library. Below you can find our Menu for several Tasks.\n***MENU***\n1) List Books\n2) Add Book\n3) Remove Book\n")

        operation_input = int(input("Enter the number of the desired operation: "))
        if  operation_input == 1:
            self.list_books()
        elif operation_input == 2:
            self.add_book(title=None, author=None, year=None, num_of_pages=None)
        elif operation_input == 3:
            try:
                remove_name = str(input("Enter the name of the book you want to remove: "))
                self.remove_book(remove_name)
            except ValueError:
                print("Invalid Input! Please enter a valid book name.")

        self.open_file()

    def open_file(self):
        with open("books.txt", "a+") as f:
            return f
        
    def list_books(self):
        with open("books.txt", 'r') as file:
            for line in file:
                self.books.append(line.strip())
        print("\n".join(self.books))
    
    def add_book(self, title, author, year, num_of_pages):
        new_book = input("Enter the details of the new book in this shape (Title, Author, Year, Number of Pages): ")
        new_book_list = list(new_book)
        title = new_book_list[0]
        author = new_book_list[1]
        year = new_book_list[2]
        pages = new_book_list[3:]

        new_book_dict = {
            "title": title,
            "author": author,
            "year": year,
            "num_of_pages": num_of_pages
        }
        self.books.append(new_book_dict.__str__())
        print("Book added successfully!\n")
        with open("books.txt", "a+") as file:
            file.write(f"\n{new_book}")
            print('books.txt file updated succesfully.')

    def remove_book(self, remove_name):
        with open('books.txt', 'r') as file:
            removed_books_list = [line.strip() for line in file]

            updated_books_list = [book for book in removed_books_list if remove_name not in book] 

            if len(updated_books_list) < len(removed_books_list):
                # Overwrite 'books.txt' file with the updated content in 'updated_books_list'
                file.seek(0)
                with open('books.txt', 'w') as file:
                    for line in updated_books_list:
                        file.write(line + '\n')  
                print(f"The Book '{remove_name}' has been removed succesfully.\n")
            else:
                print(f"The book '{remove_name}' does not exist in the library.\n")
            
if __name__ == "__main__":
    Library()