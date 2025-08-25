class Book:
    def __init__(self, title, author, isbn, year):
        self.__title = title ## 제목
        self.__author = author ## 지은이
        self.__isbn = isbn ## 고유번호
        self.__year = year ## 출판연도

    def get_title(self): ## 제목 가져오기
        return self.__title
    
    def get_author(self): ## 지은이 가져오기
        return self.__author
    
    def get_isbn(self): ## 고유번호 가져오기
        return self.__isbn
    
    def get_year(self): ## 출판연도 가져오기
        return self.__year
    
class Member:
    def __init__(self, name, id):
        self.__name = name ## 멤버 이름
        self.__id = id ## 멤버 아이디
        self.__borrowedBook = [] ## 멤버가 빌려간 책 리스트

    def get_name(self): ## 멤버 이름 가져오기
        return self.__name
    
    def get_id(self): ## 멤버 아이디 가져오기
        return self.__id
    
    def borrow_book(self, book:Book): ## 멤버의 책 리스트에 빌린 책 넣기
        self.__borrowedBook.append(book)
        
    def return_book(self, book:Book): ## 멤버의 책 리스트에서 반납한 책 빼기
        self.__borrowedBook.remove(book)

    def show_borrowed_book(self): ## 멤버가 빌린 책 리스트 중 제목 반환
        return [book.get_title() for book in self.__borrowedBook]
    
class Library:
    def __init__(self):
        self.__bookList = [] ## 도서관에 있는 책 리스트
        self.__memberList = [] ## 도서관 멤버 리스트

    def register_member(self, member:Member): ## 멤버 등록 함수
        self.__memberList.append(member) 

    def remove_member(self, member:Member): ## 멤버 제거 함수
        self.__memberList.remove(member)

    def show_member(self): ## 가입한 멤버의 이름과 빌려간 책 반환 함수
        return [
        {
            "name": member.get_name(),
            "borrowed_book": member.show_borrowed_book()
        }
        for member in self.__memberList
    ]

    def add_book(self, book:Book): ## 도서관에 추가되는 책 더하는 함수
        self.__bookList.append(book)
    
    def remove_book(self, book:Book): ## 도서관에 제거되는 책 빼는 함수
        self.__bookList.remove(book)

    def show_book_list(self): ## 도서관에 현재 있는책 반환 함수
        return [book.get_title() for book in self.__bookList]

    def search_book(self, info_book): ## 책의 제목과, 지은이, 출판연도로 도서관에 지금 책이 있는지를 검색하는 함수
        for book in self.__bookList:
            if info_book == book.get_title(): ## 도서관에 있는 책의 제목과 찾는 책의 제목이 같다면
                print("찾으시는 책이 있습니다")
            elif info_book == book.get_author(): ## 도서관에 있는 책의 지은이와 찾는 책의 지은이가 같다면
                print("찾으시는 책이 있습니다")
            elif info_book == book.get_isbn(): ## 도서관에 있는 책의 고유번호와 찾는 책의 고유번호가 같다면
                print("찾으시는 책이 있습니다")
            else: ## 아무것도 같지 않다면
                print("찾으시는 책이 없습니다")

    def borrow_book(self, member:Member, book:Book): ## 멤버가 책을 빌려가면 책을 도서관의 책 리스트에선 제거하고 멤버 리스트에 추가해주는 함수
        if book in self.__bookList: ## 책이 도서관 책 리스트에 있는지 확인
            self.__bookList.remove(book) ## 도서관 리스트에서 책 제거
            member.borrow_book(book) ## 멤버 책 리스트에 책 추가
            print(f"{book.get_title}책을 빌렸습니다")
        else: ## 빌리려는 책이 없다면
            print(f"{book.get_title()}책이 없습니다") 

    def return_book(self, member:Member, book:Book): ## 멤버가 책을 반납하면 책을 도서관의 책 리스트에 추가하고 멤버 리스트에는 제거
        if book.get_title() in member.show_borrowed_book(): ## 멤버가 반납할 책 제목이 멤버 책 리스트에 있다면
            self.__bookList.append(book) ## 도서관 책 리스트에 책 추가
            member.return_book(book) ## 멤버 책 리스트에서 책 제거
            print(f"{book.get_title}책 반납에 성공했습니다")
        else: ## 멤버 책 리스트에 반납할 책이 없다면
            print(f"{book.get_title()}책이 없어 반납에 실패했습니다")