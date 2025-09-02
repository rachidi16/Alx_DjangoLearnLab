from django.db import models

class Author(models.Model):
    """
    Author model represents a book author.
    Fields:
        name: Stores the author's name as a string.
    Purpose:
        Used to group books by their author and establish a one-to-many relationship with Book.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Book model represents a book entry.
    Fields:
        title: Stores the book's title as a string.
        publication_year: Stores the year the book was published as an integer.
        author: ForeignKey linking to Author, establishing a one-to-many relationship (one author, many books).
    Purpose:
        Used to store book details and link each book to its author.
    Relationship:
        The 'author' field uses related_name='books', allowing access to all books for an author via author.books.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title