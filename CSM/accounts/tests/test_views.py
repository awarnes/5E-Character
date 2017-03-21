import pytest
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

from pages.views import landing, CharacterCreationName


class TestHomeView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        resp = landing(req)
        assert resp.status_code == 200, 'Should be callable by anyone.'


class TestAdminView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        req.user = AnonymousUser()
        resp = CharacterCreationName.as_view()(req)
        assert 'login' in resp.url, "Should redirect to login page."

    def test_superuser(self):
        user = mixer.blend('accounts.Member', is_superuser=True)
        req = RequestFactory().get('/')
        req.user = user
        resp = CharacterCreationName.as_view()(req)
        assert resp.status_code == 200, "Should be callable by superuser."