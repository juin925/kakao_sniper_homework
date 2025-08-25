class Book:
    def __init__(self, title, author, isbn, year):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__year = year

    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_isbn(self):
        return self.__isbn
    
    def get_year(self):
        return self.__year
    
    
class Member:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
        self.__borrowedBook = []

    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def borrow_book(self, book:Book):
        self.__borrowedBook.append(book)
        

    def return_book(self, book:Book):
        self.__borrowedBook.remove(book)

    def show_borrowed_book(self):
        return [book.get_title() for book in self.__borrowedBook]
    



class Library:
    def __init__(self):
        self.__bookList = []
        self.__memberList = []

    def register_member(self, member:Member):
        self.__memberList.append(member)

    def remove_member(self, member:Member):
        self.__memberList.remove(member)

    def show_member(self):
        return [
        {
            "name": member.get_name(),
            "borrowed_book": member.show_borrowed_book()
        }
        for member in self.__memberList
    ]

    def add_book(self, book:Book):
        self.__bookList.append(book)
    
    def remove_book(self, book:Book):
        self.__bookList.remove(book)

    def show_book_list(self):
        return [book.get_title() for book in self.__bookList]

    def search_book(self, info_book):
        for book in self.__bookList:
            if info_book == book.get_title():
                print("찾으시는 책이 있습니다")
            elif info_book == book.get_author():
                print("찾으시는 책이 있습니다")
            elif info_book == book.get_isbn():
                print("찾으시는 책이 있습니다")
            else:
                print("찾으시는 책이 없습니다")


    def borrow_book(self, member:Member, book:Book):
        if book in self.__bookList:
            print(book.get_title())
            self.__bookList.remove(book)
            member.borrow_book(book)
            print(f"{book.get_title}책을 빌렸습니다")
        else:
            print(book.get_title())
            print(f"{book.get_title()}책이 없습니다")

    def return_book(self, member:Member, book:Book):
        if book.get_title() in member.show_borrowed_book():
            self.__bookList.append(book)
            member.return_book(book)
            print(f"{book.get_title}책 반납에 성공했습니다")
        else:
            print(f"{book.get_title()}책이 없어 반납에 실패했습니다")