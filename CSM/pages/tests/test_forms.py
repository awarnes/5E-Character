import pytest
from ..forms import AbilityScoresChoice
pytestmark = pytest.mark.django_db

class TestCCAbilityScores:
    def test_form(self):
        form = AbilityScoresChoice()
        assert form.is_valid() is False, "Must be invalid with no data."

        data = {'Strength': 15}
        form = AbilityScoresChoice(data=data)
        assert form.is_valid() is False, "Must fill all parts of form"
        assert 'Dexterity' in form.errors, "Must return a few error fields."

        data = {'Strength': 10, 'Dexterity': 10, 'Constitution': 10, 'Intelligence': 10, 'Wisdom': 10, 'Charisma': 10}
        form = AbilityScoresChoice(data=data)
        assert form.is_valid() is True, "Must be valid when all data is given."
