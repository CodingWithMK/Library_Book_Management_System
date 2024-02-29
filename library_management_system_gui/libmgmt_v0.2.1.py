import customtkinter
from tkinter import *

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

HEIGHT = 540
WIDTH = 960

books_list = []

class Library(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{WIDTH}x{HEIGHT}")
        
        self.title("Library Management System")

        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.item_frame = customtkinter.CTkFrame(self)
        self.item_frame.grid(row=0, column=0, sticky="w")

        # Create a text widget to display the content
        self.text_widget = Text(self.item_frame, wrap="word", height=10, width=60)
        self.text_widget.grid(row=0, column=0)

        # Creating a button to open the text file
        self.open_button = customtkinter.CTkButton(self.item_frame, text="Open", command=self.open_file)
        self.open_button.grid(row=1, column=0, sticky='w')

        # Creating a button to update text_widget content
        self.update_button = customtkinter.CTkButton(self.item_frame, text='Update', command=self.update_library)
        self.update_button.grid(row=1, column=0, sticky='e')

        # Adding scrollbar to the text widget
        self.scrollbar = customtkinter.CTkScrollbar(self.item_frame, orientation='vertical')
        self.scrollbar.grid(row=0, column=3, sticky='ns')
        self.text_widget.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.text_widget.yview)

        self.action_buttons_frame = customtkinter.CTkFrame(self)
        self.action_buttons_frame.grid(row=2, column=2, sticky='e')
        
        self.add_book_button = customtkinter.CTkButton(self.action_buttons_frame, text="Add Book", command=self.add_book_window)
        self.add_book_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.delete_book_button = customtkinter.CTkButton(self.action_buttons_frame, text="Delete Book", command=self.remove_book_window)
        self.delete_book_button.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        # self.book_details_entry = customtkinter.CTkEntry(self, width=30)
        # self.book_details_label = Label(master=self.item_frame, textvariable=self.book_details_entry)

        
        self.open_file()

    
    # Function to open a text file and display its content
    def open_file(self):
        books_file = 'library_management_system_gui/libmgmtsys_books.txt'
        if books_file:
                with open(books_file, "r") as file:
                    content = file.read()
                    self.text_widget.delete("1.0", "end")
                    self.text_widget.insert("1.0", content)

    
    def update_library(self):
        """Updateing library by writing new content into the 'libmgmtsys_books.txt' file."""
        updated_content = self.text_widget.get('1.0', END)
        with open('library_management_system_gui/libmgmtsys_books.txt', 'w') as lib_content:
            lib_content.write(updated_content)
        


    def add_book_window(self):
        self.add_window = customtkinter.CTkToplevel(self)
        self.add_window.geometry("600x250")
        self.add_window.title("Add Book")

        self.title_label = customtkinter.CTkLabel(self.add_window, text="Enter the title of your new book:")
        self.title_entry = customtkinter.CTkEntry(self.add_window, width=300)
        self.author_label = customtkinter.CTkLabel(self.add_window, text="Enter the author's name:")
        self.author_entry = customtkinter.CTkEntry(self.add_window, width=180)
        self.year_label = customtkinter.CTkLabel(self.add_window, text="Enter the first production year:")
        self.year_entry = customtkinter.CTkEntry(self.add_window, width=180)
        self.num_of_pages_label = customtkinter.CTkLabel(self.add_window, text="Enter the number of pages:")
        self.num_of_pages_entry = customtkinter.CTkEntry(self.add_window, width=180)
        self.confirm_button = customtkinter.CTkButton(self.add_window, text="Add", command=lambda: self.add_confirmation(
            self.title_entry.get(),
            self.author_entry.get(),
            int(self.year_entry.get()),
            int(self.num_of_pages_entry.get()),
            self.add_window
        ))
        self.cancel_button = customtkinter.CTkButton(self.add_window, text="Cancel", command=self.add_window.destroy)

        self.title_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.title_entry.grid(row=0, column=1, padx=(20,10), pady=10, sticky='w')
        self.author_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.author_entry.grid(row=1, column=1, padx=(20,10), sticky='w')
        self.year_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.year_entry.grid(row=2, column=1, padx=(20, 10), pady=10, sticky='w')
        self.num_of_pages_label.grid(row=3, column=0,padx=10, pady=10, sticky='w')
        self.num_of_pages_entry.grid(row=3, column=1, padx=(20, 10), pady=10, sticky='w')
        self.confirm_button.grid(row=4, column=1, padx=10, pady=10, sticky='w')
        self.cancel_button.grid(row=4, column=0, padx=10, pady=10, sticky='w')

    def add_confirmation(self, title, author, year, num_of_pages):
        if not (title and author and year and num_of_pages):
            print("Error", "Please fill out all fields.")
        else:
            book_info = f"{title}, {author}, {year}, {num_of_pages}"
            self.text_widget.insert(END, book_info)
            print(f'The book {title} successfully added.')
            self.add_window.destroy()


    def remove_book_window(self):
        self.remove_window = customtkinter.CTkToplevel(self)
        self.remove_window.geometry("400x150")
        self.remove_window.title('Delete Book')

        self.remove_book_entry_label = customtkinter.CTkLabel(self.remove_window, text='Enter the book title you want to delete:')
        self.remove_book_entry = customtkinter.CTkEntry(self.remove_window, width=180)
        self.remove_button = customtkinter.CTkButton(self.remove_window, text='Delete', command=lambda: self.delete_confirmation(
            self.remove_book_entry.get(),
        ))
        
        self.remove_book_entry_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.remove_book_entry.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.remove_button.grid(row=2, column=0, padx=10, pady=10, sticky='w')

    
    def delete_confirmation(self, remove_book):

        for index in range(self.text_widget.size()[0]):
            if remove_book in self.text_widget.get(index + 1.0, index +  1.0 + 'lineend'):
                self.text_widget.delete(index + 1.0, index +  1.0 + 'lineend')
                self.remove_window.destroy()
                return
        
        print(f"The book '{remove_book}' does not exist")



if __name__ == "__main__":
    app = Library()
    app.mainloop()
