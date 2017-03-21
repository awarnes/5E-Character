import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db


class TestCharacter:
    def test_init(self):
        character = mixer.blend('character.Character')
        assert character.pk == 1, 'Should save an instance.'