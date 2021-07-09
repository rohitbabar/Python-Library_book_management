class Library:
    def __init__(self, Listofbooks):
        self.books = Listofbooks

    def Available_books(self):
        print("Available books in the library :")
        for i, books in enumerate(self.books, start=1):
            print(f'{i}) {books}')

    def borrow_book(self, book):
        if book in self.books:
            print(
                f"You have been issued the book {book}. Must return it within 30 days")
            self.books.remove(book)
            return True
        else:
            print("The book you requested is not available")
            return False

    def return_book(self, book):
        print("thank you for returning it!! hope u enjoyed it!!")
        self.books.append(book)


class student:
    def request_book(self):
        self.book = input('Enter book u want:')
        return self.book

    def return_book(self):
        self.book = input('Enter book u want to return:')
        return self.book


if __name__ == '__main__':
    Kalyan_library = Library(
        ['Algebra', 'Polity', 'to be RICH', 'wonders', 'nights out'])
    reader = student()
    while(True):
        welcomMsg = '''        
        <<<<<<<<********WELCOME TO KALYAN LIBRARY********>>>>>>>>
        Please select one of the following option:
        1) List of all available books
        2) requeat a book
        3) return a book
        4) exit

        '''
        print(welcomMsg)
        a = (input("\t Enter your choice  :"))
        print()
        if a == str(1):
            Kalyan_library.Available_books()
        elif a == str(2):
            Kalyan_library.borrow_book(reader.request_book())
        elif a == str(3):
            Kalyan_library.return_book(reader.return_book())
        elif a == str(4):
            print("THANKU FOR CHOSING KALYAN LIBRARY")
            exit()
        else:
            print("invalid choice")
