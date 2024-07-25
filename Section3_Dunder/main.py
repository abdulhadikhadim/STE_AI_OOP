class Book:
    def __init__(self,title,author,book_type,pages):
        self.title = title
        self.author = author
        self.book_type = book_type
        self.pages = pages 
    
    #if we add the __repr__ we can customize our class instance

    def __repr__(self):
        return f"The author of the book is {self.author}"

    def __str__(self):
        return f"The book {self.book_type} is written by {self.author}"

    def __format__(self,format_spec):
        if format_spec =="short":
            return f"{self.title}, {self.author}"
        elif format_spec == "stealth":
            return f"the book contain exactly {self.pages} "
        return repr(self)


b = Book("Hello","Ghalib","Poetry",574) #this is the object of the main class Book
x = format(b,"stealth")
print(x)
print(f"{b:short}")
print(f"{b:stealth}")