import customtkinter
from tkinter import *

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

class Library(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Library Management System")

        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.item_frame = customtkinter.CTkFrame(self)
        self.item_frame.grid(row=0, column=1, sticky="n")

        # Create a button to open a text file
        self.open_button = customtkinter.CTkButton(self.item_frame, text="Open Library", command=self.open_file)
        self.open_button.grid(row=1, column=0)

        # Create a text widget to display the content
        self.text_widget = Text(self.item_frame, wrap="word", height=10, width=60)
        self.text_widget.grid(row=0, column=0)

    
    # Function to open a text file and display its content
    def open_file(self):
        books_file = 'books.txt'
        if books_file:
                with open(books_file, "r") as file:
                    content = file.read()
                    self.text_widget.delete("1.0", "end")
                    self.text_widget.insert("1.0", content)

    

if __name__ == "__main__":
    app = Library()
    app.mainloop()
