from book import Book

library = [Book("Птицы", "Дафна Дюморье"),
           Book("Король в желтом", "Роберт Чамберс"),
           Book("Моя семья и другие звери", "Джеральд Даррелл")]

for book in library:
    print(f"{book.title} - {book.author}")
