from __future__ import annotations

from typing import Any, Self

from graphene import ID, Boolean, Field, List, Mutation, ObjectType, Schema, String
from graphene_django import DjangoObjectType

from .models import Author, Post


class PostType(DjangoObjectType):
    """Type for the Post model. This class will map the Post model to a GraphQL type."""

    class Meta:  # noqa: D106
        model = Post
        fields = "__all__"


class AuthorType(DjangoObjectType):
    """Type for the Author model. This class will map the Author model to a GraphQL type."""

    class Meta:  # noqa: D106
        model = Author
        fields = "__all__"


class CreatePost(Mutation):
    """Create a new post."""

    class Arguments:  # noqa: D106
        title = String(required=True)
        content = String(required=True)
        author_id = ID(required=True)

    post = Field(PostType)

    def mutate(self: Self, info: Any, title: str, content: str, author_id: int) -> Self:  # noqa: ANN401, ARG002
        """Mutate function for the CreatePost mutation.

        The mutate function is the function that will be called when a client
        makes a request to this mutation. It takes in four arguments:
        self, info, title and content. The first two are required by all mutations;
        the last two are the arguments we defined in our CreatePostInput class.

        Args:
            self (Self): Access the object's attributes and methods
            info (Any): Access the context of the request
            title (str): Create a new post with the title provided
            content (str): Pass the content of the post
            author_id (int): Get the author object from the database

        Returns:
            Self: A createpost object
        """
        author = Author.objects.get(pk=author_id)
        post = Post(title=title, content=content, author=author)
        post.save()
        return CreatePost(post=post)


class UpdatePost(Mutation):
    """Update an existing post."""

    class Arguments:  # noqa: D106
        id = ID(required=True)
        title = String()
        content = String()

    post = Field(PostType)

    def mutate(self: Self, info: Any, id: int, title: None | str = None, content: None | str = None) -> Self:  # noqa: A002, ANN401, ARG002
        """Mutate function for the UpdatePost mutation.

        The mutate function is the function that will be called when a client
        calls this mutation. It takes in four arguments: self, info, id and title.
        The first two are required by all mutations and the last two are specific to this mutation.
        The self argument refers to the class itself (UpdatePost) while info contains information about
        the query context such as authentication credentials or access control lists.

        Args:
            self (Self): Pass the instance of the class
            info (Any): Access the context of the request
            id (int): Find the post we want to update
            title (None | str, optional): Update the title of a post. Defaults to None.
            content (None | str, optional): Update the content of a post. Defaults to None.

        Raises:
            Exception: If the post is not found, raise an exception

        Returns:
            _type_: An instance of the updatepost class, which is a subclass of mutation
        """
        try:
            post = Post.objects.get(pk=id)
        except Post.DoesNotExist as e:
            msg = "Post not found"
            raise Exception(msg) from e  # noqa: TRY002

        if title is not None:
            post.title = title
        if content is not None:
            post.content = content

        post.save()
        return UpdatePost(post=post)


class DeletePost(Mutation):
    """Delete an existing post."""

    class Arguments:  # noqa: D106
        id = ID(required=True)

    success = Boolean()

    def mutate(self: Self, info: Any, id: int) -> Self:  # noqa: A002, ANN401, ARG002
        """Mutate function for the DeletePost mutation.

        The mutate function is the function that will be called when a client
        calls this mutation. It takes in four arguments: self, info, id. The first
        argument is the object itself (the class instance). The second argument is
        information about the query context and user making this request. We don't
        need to use it here so we'll just pass it along as-is to our model method.
        The third argument is an ID of a post we want to delete.

        Args:
            self (Self): Represent the instance of the class
            info (Any): Access the context of the query
            id (int): Find the post that is to be deleted

        Raises:
            Exception: If the post is not found, raise an exception

        Returns:
            Self: A deletepost object, which is the return type of the mutation
        """
        try:
            post = Post.objects.get(pk=id)
        except Post.DoesNotExist as e:
            msg = "Post not found"
            raise Exception(msg) from e  # noqa: TRY002

        post.delete()
        return DeletePost(success=True)


class Query(ObjectType):
    """Query class for the schema."""

    posts = List(PostType)
    authors = List(AuthorType)

    def resolve_posts(self: Self, info: Any) -> PostType:  # noqa: ARG002, ANN401
        """The resolve_posts function is a resolver.

        It's responsible for retrieving the posts from the database and returning them to GraphQL.

        Args:
            self (Self): Refer to the current instance of a class
            info (Any): Pass along the context of the query

        Returns:
            PostType: All post objects from the database
        """
        return Post.objects.all()

    def resolve_authors(self: Self, info: Any) -> AuthorType:  # noqa: ARG002, ANN401
        """The resolve_authors function is a resolver.

        It's responsible for retrieving the data that will be returned as part of an execution result.

        Args:
            self (Self): Pass the instance of the object to be used
            info (Any): Pass information about the query to the resolver

        Returns:
            AuthorType: A list of all the authors in the database
        """
        return Author.objects.all()


class Mutation(ObjectType):
    """Mutation class for the schema."""

    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()


schema = Schema(query=Query, mutation=Mutation)
