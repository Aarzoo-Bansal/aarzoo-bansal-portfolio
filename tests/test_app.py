# tests/test_app.py

import unittest
import os
os.environ['TESTING'] = 'true'

from app import TimelinePost, app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        TimelinePost.delete().execute()

    def tearDown(self):
        TimelinePost.delete().execute()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Aarzoo Bansal</title>" in html
        # TODO Add more tests relating to the home page
        assert "<h1>Aarzoo Bansal</h1>" in html
        assert "<h2>About Me</h2>" in html
        assert '<a href="/experience"' in html
        assert '<a href="/education"' in html
        assert '<a href="/hobbies"' in html
        assert '<a href="/map"' in html
        assert '<a href="/timeline"' in html

    def test_timeline_api(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        payload = response.get_json()
        assert payload == {"timeline_posts": []}

        response = self.client.post("/api/timeline_post", data={
            "name": "Test User",
            "email": "test@example.com",
            "content": "This is a test post"
        })
        assert response.status_code == 200
        assert response.is_json
        post = response.get_json()
        assert post["name"] == "Test User"
        assert post["email"] == "test@example.com"
        assert post["content"] == "This is a test post"

        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        posts = response.get_json()["timeline_posts"]
        assert len(posts) == 1
        assert posts[0]["name"] == "Test User"
        assert posts[0]["email"] == "test@example.com"
        assert posts[0]["content"] == "This is a test post"

    def test_timeline_page(self):
        response = self.client.get("/timeline")
        assert response.status_code == 200

        html = response.get_data(as_text=True)
        assert "<title>Timeline</title>" in html
        assert "<h1>Timeline</h1>" in html
        assert 'id="timeline-form"' in html
        assert 'name="name"' in html
        assert 'name="email"' in html
        assert 'name="content"' in html
        assert 'id="posts"' in html

    def test_delete_timeline_post(self):
        post = TimelinePost.create(
            name="Test User",
            email="test@example.com",
            content="Delete me",
        )

        response = self.client.delete(f"/api/timeline_post/{post.id}")
        assert response.status_code == 200
        assert response.get_json() == {
            "message": f"Timeline post {post.id} deleted successfully"
        }
        assert TimelinePost.get_or_none(TimelinePost.id == post.id) is None

    def test_delete_missing_timeline_post(self):
        response = self.client.delete("/api/timeline_post/999")
        assert response.status_code == 404
        assert response.get_json() == {
            "error": "Timeline post with id 999 not found"
        }

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post(
            "/api/timeline_post",
            data={
                "email": "john@example.com",
                "content": "Hello world, I'm John!"
            }
        )
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post(
            "/api/timeline_post",
            data={
                "name": "John Doe",
                "email": "john@example.com",
                "content": ""
            }
        )
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST requests with malformed email addresses
        for email in ("not-an-email", "@example.com", "john@", "john@@example"):
            with self.subTest(email=email):
                response = self.client.post(
                    "/api/timeline_post",
                    data={
                        "name": "John Doe",
                        "email": "email",
                        "content": "Hello world, I'm John!"
                    }
                )
                assert response.status_code == 400
                assert response.get_json() == {"error": "Invalid email"}
