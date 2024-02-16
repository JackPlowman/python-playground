import pytest

from blog.models import Author, Post

TEST_AUTHOR = "Test Author"
TEST_POST = "Test Post"
TEST_CONTENT = "Test Content"


@pytest.mark.django_db()
def test_author_attributes() -> None:
    author = Author.objects.create(name=TEST_AUTHOR)
    assert author.id is not None
    assert Author._meta.get_field("id").primary_key
    assert Author._meta.get_field("id").serialize is False
    assert Author._meta.get_field("id").verbose_name == "ID"
    assert author.name == TEST_AUTHOR
    assert Author._meta.get_field("name").max_length == 100


@pytest.mark.django_db()
def test_author_str() -> None:
    author = Author.objects.create(name=TEST_AUTHOR)
    assert str(author) == TEST_AUTHOR


@pytest.mark.django_db()
def test_post_attributes() -> None:
    author = Author.objects.create(name=TEST_AUTHOR)
    post = Post.objects.create(title=TEST_POST, content=TEST_CONTENT, author=author)
    assert post.id is not None
    assert Post._meta.get_field("id").primary_key
    assert Post._meta.get_field("id").serialize is False
    assert Post._meta.get_field("id").verbose_name == "ID"
    assert post.title == TEST_POST
    assert Post._meta.get_field("title").max_length == 100
    assert post.content == TEST_CONTENT
    assert post.author == author


@pytest.mark.django_db()
def test_post_str() -> None:
    author = Author.objects.create(name=TEST_AUTHOR)
    post = Post.objects.create(title=TEST_POST, content=TEST_CONTENT, author=author)
    assert str(post) == TEST_POST
