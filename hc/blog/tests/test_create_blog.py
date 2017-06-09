"""Test cases for testing create_blog functionality."""

from hc.test import BaseTestCase


class CreateBlogTestCase(BaseTestCase):
    """Test class for create_blog tests."""

    def test_only_logged_in_user_can_create_blog(self):
        """Tests if only logged in users can access the create blog page."""
        pass

    def test_cannot_create_blog_if_not_logged_in(self):
        """Tests if a user cannot access the create_blog page if they are not logged in.""" # noqa
        pass

    def test_it_created_blog_is_saved(self):
        """Tests if a blog created is saved in the db."""
        pass
