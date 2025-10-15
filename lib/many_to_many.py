class Author:
    """Represents a writer who can sign many book contracts."""
    all = []

    def __init__(self, name: str):
        if not isinstance(name, str):
            raise Exception("name must be a str")
        self.name = name
        Author.all.append(self)

    def contracts(self):
        """Return all Contract objects that belong to this author."""
        return [c for c in Contract.all if c.author is self]

    def books(self):
        """Return all Book objects linked to this author via contracts."""
        return [c.book for c in Contract.all if c.author is self]

    def sign_contract(self, book, date, royalties):
        """
        Create and return a new Contract for this author.
        """
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Sum all royalties from this author's contracts."""
        return sum(c.royalties for c in self.contracts())

class Book:
    """Represents a book that can have contracts with many authors."""
    all = []

    def __init__(self, title: str):
        if not isinstance(title, str):
            raise Exception("title must be a str")
        self.title = title
        Book.all.append(self)

    def contracts(self):
        """Return all Contract objects that belong to this book."""
        return [c for c in Contract.all if c.book is self]

    def authors(self):
        """Return all Author objects linked to this book via contracts."""
        return [c.author for c in self.contracts()]

class Contract:
    """
    Intermediary (joining) class for the many-to-many relation
    between Author and Book. It stores extra data like date/royalties.
    """
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an Author instance")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be a Book instance")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be a str")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("royalties must be an int")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date_str):
        """Return all contracts whose date equals the given date string."""
        return [c for c in cls.all if c.date == date_str]