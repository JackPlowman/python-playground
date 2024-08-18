import pytest
from graphene.test import Client

from blog.models import Author, Post
from blog.schema import schema


@pytest.fixture
def client() -> Client:
    return Client(schema)


@pytest.fixture
def author() -> Author:
    return Author.objects.create(name="Test Author")


@pytest.fixture
def post(author: Author) -> Post:
    return Post.objects.create(title="Test Post", content="Test Content", author=author)


@pytest.mark.django_db
def test_create_post(client: Client, author: Author) -> None:
    mutation = f"""
        mutation {{
            createPost(title: "Test Post", content: "Test Content", authorId: {author.id}) {{
                post {{
                    title
                    content
                    author {{
                        id
                    }}
                }}
            }}
        }}
    """
    expected = {
        "createPost": {"post": {"title": "Test Post", "content": "Test Content", "author": {"id": str(author.id)}}}
    }
    result = client.execute(mutation)
    assert result["data"] == expected


@pytest.mark.django_db
def test_update_post(client: Client, post: Post) -> None:
    mutation = f"""
        mutation {{
            updatePost(id: {post.id}, title: "Updated Title", content: "Updated Content") {{
                post {{
                    title
                    content
                }}
            }}
        }}
    """
    expected = {
        "updatePost": {
            "post": {
                "title": "Updated Title",
                "content": "Updated Content",
            }
        }
    }
    result = client.execute(mutation)
    assert result["data"] == expected


@pytest.mark.django_db
def test_delete_post(client: Client, post: Post) -> None:
    mutation = f"""
        mutation {{
            deletePost(id: {post.id}) {{
                success
            }}
        }}
    """
    expected = {
        "deletePost": {
            "success": True,
        }
    }
    result = client.execute(mutation)
    assert result["data"] == expected
