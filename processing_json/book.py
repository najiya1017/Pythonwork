from json import load

f=open("D:\\python\\luminar\\datasets\\datasets_json\\book.json")

data=load(f)

# for book in data:

#     print(book)

all_book_title=[book.get("title") for book in data]

# print(all_book_title)

page_filter=[book.get("title") for book in data if book.get("pages")<250]

# print(page_filter)

all_genres={book.get("genre") for book in data}

# print(all_genres)

book_cost=max(data,key=lambda book:book.get("price")) #max cost

# print(book_cost)

#author with more than one book

all_author=[book.get("author") for book in data]

more_than_one=[auth for auth in all_author if all_author.count(auth)>1]

print(set(more_than_one))