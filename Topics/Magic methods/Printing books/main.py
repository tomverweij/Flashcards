class Book:
    def __init__(self, author, title, price, book_id):
        self.author = author
        self.title = title
        self.price = price
        self.book_id = book_id

    def __str__(self):
        return '{} by {}. ${}. [{}]'.format(self.title, self.author,
                                            self.price, self.book_id)

    # For
    # instance,
    # if we have Book("George Orwell", "1984", 13.59, 1956789),
    # the method should return 1984 by George Orwell.$13.59.[1956789].