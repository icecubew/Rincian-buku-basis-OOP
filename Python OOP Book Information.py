class book:
    def __init__(self, isbn, title, author, publisher, pages, harga, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = harga
        self.copies = copies

    def view(self):
        print("ISBN: ", self.isbn)
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Publisher: ", self.publisher)
        print("Pages: ", self.pages)
        print("Price: ", self.price)
        print("Copies: ", self.copies)

book1 = book("979-3062-79-7", "Laskar Pelangi", "Andrea Hirata", "Bentang Pustaka", 529,  'Rp. 100.000', 100)
book2 = book("978-979-1227-02-5", "Edensor", "Andrea Hirata", "Bentang Pustaka", 304, 'Rp. 90.000', 50)
book3 = book("111-222-333", "Pride and Prejudice", "Jane Austen", "Penguin Books", 210, 'Rp. 120.000', 60)
book4 = book("444-555-666", "1984", "George Orwell", "Penguin Books", 300, 'Rp. 100.000', 70)

print("=" *9 + " Daftar Buku " + "=" *9)
print("")

book1.view()
print("")
print("="*30)

book2.view()

print("")
print("="*30)

book3.view()
print("")
print("="*30)

book4.view()
