from api.posts_client import PostsClient


client = PostsClient()


def test_get_all_posts():
    response = client.get_all_posts()

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0


def test_get_single_post():
    response = client.get_post(1)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
    assert "userId" in data


def test_create_post():
    payload = {
        "title": "Test title",
        "body": "Test body",
        "userId": 1
    }

    response = client.create_post(payload)

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]


def test_update_post():
    payload = {
        "id": 1,
        "title": "Updated title",
        "body": "Updated body",
        "userId": 1
    }

    response = client.update_post(1, payload)

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Updated title"


def test_delete_post():
    response = client.delete_post(1)

    assert response.status_code == 200


# Negative Test
def test_get_invalid_post():
    response = client.get_post(99999)

    assert response.status_code == 404 or response.json() == {}