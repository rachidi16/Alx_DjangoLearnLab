from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Serializes all fields of the Book model.
    Includes custom validation to ensure publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Ensure the publication year is not in the future.
        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Serializes the name field and includes a nested list of related books using BookSerializer.
    Demonstrates the one-to-many relationship between Author and Book.
    """
    books = BookSerializer(many=True, read_only=True)  # 'books' uses related_name from Book model

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

    # The nested BookSerializer allows dynamic serialization of all books for each author.