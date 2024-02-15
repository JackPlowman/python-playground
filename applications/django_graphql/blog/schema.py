import graphene
from graphene_django import DjangoObjectType

from .models import Author, Post


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = "__all__"


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = "__all__"


class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)
        author_id = graphene.ID(required=True)
