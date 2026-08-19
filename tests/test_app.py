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
        # every field is marked required so the browser blocks empty submits too
        assert '<input type="text" name="name" placeholder="Your name" required>' in html
        assert '<input type="email" name="email" placeholder="Your email" required>' in html
        assert 'name="content" placeholder="What\'s on your mind?" required>' in html
        # and the server's rejection message has somewhere to render
        assert 'id="form-error"' in html

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
                        "email": email,
                        "content": "Hello world, I'm John!"
                    }
                )
                assert response.status_code == 400
                assert response.get_json() == {"error": "Invalid email"}

    def test_empty_timeline_post_is_rejected(self):
        valid = {
            "name": "John Doe",
            "email": "john@example.com",
            "content": "Hello world, I'm John!"
        }

        # Each field on its own: empty, whitespace-only, or missing entirely
        for field in ("name", "email", "content"):
            for blank in ("", "   ", "\t\n"):
                with self.subTest(field=field, blank=repr(blank)):
                    data = dict(valid, **{field: blank})
                    response = self.client.post("/api/timeline_post", data=data)
                    assert response.status_code == 400
                    assert response.get_json() == {"error": f"Invalid {field}"}

            with self.subTest(field=field, blank="missing"):
                data = {k: v for k, v in valid.items() if k != field}
                response = self.client.post("/api/timeline_post", data=data)
                assert response.status_code == 400
                assert response.get_json() == {"error": f"Invalid {field}"}

        # An entirely empty form reports all three fields at once
        response = self.client.post("/api/timeline_post", data={})
        assert response.status_code == 400
        assert response.get_json() == {"error": "Invalid name, email, content"}

        # None of the rejected submissions were saved
        assert TimelinePost.select().count() == 0
        response = self.client.get("/api/timeline_post")
        assert response.get_json() == {"timeline_posts": []}

    def test_timeline_post_fields_are_stripped(self):
        response = self.client.post(
            "/api/timeline_post",
            data={
                "name": "  John Doe  ",
                "email": "  john@example.com\n",
                "content": "\t Hello world, I'm John! "
            }
        )
        assert response.status_code == 200

        post = response.get_json()
        assert post["name"] == "John Doe"
        assert post["email"] == "john@example.com"
        assert post["content"] == "Hello world, I'm John!"
