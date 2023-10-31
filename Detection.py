# Реализуйте функцию find_where(). Она должна принимать на вход список книг и поисковый запрос, а затем возвращать первую книгу, которая соответствует запросу. Каждая книга в списке — это словарь, содержащий ее параметры. Поисковый запрос — тоже словарь с параметрами.

# Если совпадений не было, то функция должна вернуть None.

# books = [
#     {'title': 'Book of Fooos', 'author': 'Foo', 'year': 1111},
#     {'title': 'Cymbeline', 'author': 'Shakespeare', 'year': 1611},
#     {'title': 'The Tempest', 'author': 'Shakespeare', 'year': 1611},
#     {'title': 'Book of Foos Barrrs', 'author': 'FooBar', 'year': 2222},
#     {'title': 'Still foooing', 'author': 'FooBar', 'year': 333},
#     {'title': 'Happy Foo', 'author': 'FooBar', 'year': 4444},
# ]

# find_where(books, {'author': 'Shakespeare', 'year': 1611})
# # {'title': 'Cymbeline', 'author': 'Shakespeare', 'year': 1611}

def find_where(books, query):
    for book in books:
        match = True
        for key, value in query.items():
            if key not in book or book[key] != value:
                match = False
                break
        if match:
            return book
    return None

# Пример использования:
books = [
    {'title': 'Book of Fooos', 'author': 'Foo', 'year': 1111},
    {'title': 'Cymbeline', 'author': 'Shakespeare', 'year': 1611},
    {'title': 'The Tempest', 'author': 'Shakespeare', 'year': 1611},
    {'title': 'Book of Foos Barrrs', 'author': 'FooBar', 'year': 2222},
    {'title': 'Still foooing', 'author': 'FooBar', 'year': 333},
    {'title': 'Happy Foo', 'author': 'FooBar', 'year': 4444},
]

result = find_where(books, {'author': 'Shakespeare', 'year': 1611})
print(result)  # {'title': 'Cymbeline', 'author': 'Shakespeare', 'year': 1611}
