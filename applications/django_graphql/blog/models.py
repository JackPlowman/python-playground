from typing import Self

from django.db.models import CASCADE, CharField, ForeignKey, Model, TextField


class Author(Model):
    """Model representing an author."""

    name = CharField(max_length=100)
    # ... other fields

    def __str__(self: Self) -> str:
        """String for representing the Model object."""
        return self.name


class Post(Model):
    """Model representing a blog post."""

    title = CharField(max_length=100)
    content = TextField()
    author = ForeignKey(Author, on_delete=CASCADE)
    # ... other fields

    def __str__(self: Self) -> str:
        """String for representing the Model object."""
        return self.title
