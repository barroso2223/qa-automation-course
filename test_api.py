import requests, pytest


@pytest.fixture
def post_get():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    return response


def test_get(post_get):

    assert post_get.status_code == 200


def test_response(post_get):

    assert "title" in post_get.json()


def test_get_id(post_get):

    assert post_get.json()["id"] == 1


def test_get_user(post_get):
    assert post_get.json()["userId"] == 1


def test_get_all():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert len(response.json()) > 50


@pytest.fixture
def created_post():
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json={"title": "My Post", "body": "My content", "userId": 1},
    )
    return response


def test_create_post(created_post):
    assert created_post.status_code == 201
