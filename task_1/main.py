#1 вариант Andrey Rudz
print("start code ...")
books = []
for i in range(5):
    title = input(f"{i+1})Введите вашу люимую книгу")
    author=input(f"{i+1})Введите автора книги")
    year = input(f"{i+1})Введите год издания книги")
    books.append(dict(title_book = title,author_book = author,year_book = year))
for i in range(5):
    print(f'''
---------------------- Книга {i+1} -----------------------
 Название: {books[i]['title_book']}, Автор: {books[i]['author_book']},
 -------------------------{books[i]['year_book']}-------------------------
 \n''')