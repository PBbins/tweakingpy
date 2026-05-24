even = []
odd = []
for i in range(1, 10):
    if i % 2 == 0:
        even.append(i)

    else:
        odd.append(i)

print(f"even {even} \n odd{odd}")

 #REVERSE NUMBER   
num = 10
while num > 0:
    print(num)
    num = num -1


#DICTIONARY LOOP
book = {"id": 12}
print(book)

book["name"] = "test1"
print(book)
book.update({"author":"prativa"})
print(book)
for i in book.values():
    print(i)
books = {"book1":dict(book),
         "book2":{"price": 100}}
print(books)