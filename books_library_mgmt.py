class Library:
    def __init__(self):

        self.books = []
        self.removed_book_list = []

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
        
        # full_book_info = ", ".join([title, author, str(year), ', '.join(map(str, pages))])
        # self.books.append(full_book_info)
        # with open('books.txt', 'a+') as file:
        #     file.write('\n' + full_book_info)

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
        with open('books.txt', 'a+') as file:
            removed_books_list = file.readlines()
            
            # Remove book from 'removed_books_list' if existing
            removed = False
            updated_books_list = []
            for line in removed_books_list:
                if remove_name not in line:
                    updated_books_list.append(line)
                else:
                    removed = True

            if removed:
                # Overwrite 'books.txt' file with the updated content in 'updated_books_list'
                file.seek(0)
                file.truncate()
                for item in updated_books_list:
                    file.write(item)  
                print(f"The Book '{remove_name}' has been removed succesfully.\n")
            else:
                    print(f"The book '{remove_name}' does not exist in the library.")
            
if __name__ == "__main__":
    Library()
        



# library = Library()

# # library.open_file()
# library.list_books()
# print('\nAdd a new Book:\nTitle: ')
# title = input()
# print('Author: ')
# author = input()
# print('Year: ')
# year = int(input())
# library.add_book(title, author, year)

# print('\nList of Books after adding the new one:\n')
# library.list_books()

# print('\nRemove a Book by its Index (enter q to exit):\nIndex: ')
# while True:
#     try:
#         input = str(input())
#         if input == -1:
#             break
#         library.remove_book(input)
#     except ValueError:
#         print("\nInvalid Input!\nPlease enter an integer value.")