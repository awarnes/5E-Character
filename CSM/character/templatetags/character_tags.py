"""
Custom Template Tags for the Character Model. General use is to invoke functions that require more than one arg.
"""

from django import template
from character.models import ClassLevel

from rules.models import Language, Skill

register = template.Library()


@register.simple_tag()
def ab_bonus(character, ability):
    return character.get_ability_bonus(ability)


@register.simple_tag()
def passive_bonus(character, ability):
    return character.get_passive_score(ability)


@register.simple_tag()
def saving_throw_bonus(character, ability):
    return character.get_saving_throw_bonus(ability)


@register.simple_tag()
def prestige_check(character):
    """Check if a character has a prestige class. Otherwise, don't display information on the page."""

    if len(character.char_prestige_classes.all()) == 0:
        return False
    else:
        return True


@register.simple_tag()
def get_languages(character):
    """Gets all languages a character is able to understand."""

    languages = [lang for lang in character.char_traits.all() if isinstance(lang, Language)]

    return languages


@register.simple_tag()
def check_skill(character, query_skill):
    """Checks if a character is proficient with a skill."""

    char_skills = character.features.filter(name__startswith='Skill:')

    for thing in char_skills:
        if query_skill in thing.name:
            return True

    return False


@register.simple_tag()
def get_skill_bonus(character, query_skill):
    """Returns the skill bonus."""

    if check_skill(character, query_skill):
        return character.get_ability_bonus(Skill.objects.get(name=query_skill).associated_ability) + character.get_prof_bonus()
    else:
        return character.get_ability_bonus(Skill.objects.get(name=query_skill).associated_ability)


@register.simple_tag()
def get_class_features(character):
    """
    Get all the class features a character has and sort them by class and level for display.
    
    :Usage:
    
    <p>Class:</p>
    {% get_class_features character as features_dict %}
    {% for class, features in features_dict.items %}
        <p>{{ class }}</p>
        <ul>
            {% for feature in features %}
                <li class="list-group-item">({{ feature.prereq_class_level }}) {{ feature }}</li>
            {% endfor %}
        </ul>
    {% endfor %}
                            
    """


    sorted_features = list()
    unsorted_features = list()
    character_features = dict()

    clevel = ClassLevel.objects.filter(character=character)

    for klass in clevel:
        unsorted_features = klass.char_class.features.all()
        sorted_features = sorted(unsorted_features, key=lambda k: k.prereq_class_level)
        character_features[klass.char_class.name] = sorted_features

    return character_features


@register.simple_tag()
def get_prestige_features(character):
    """
    Get all the prestige features a character has and sort them by prestige class and level for display.
    
    :Usage:
    
    {% prestige_check character as p %}
    {% if p %}
        <p>Prestige Class:</p>
        {% get_prestige_features character as features_dict %}
        {% for prestige, features in features_dict.items %}
            <p>{{ prestige }}</p>
            <ul>
                {% for feature in features %}
                    <li class="list-group-item">({{ feature.prereq_class_level }}) {{ feature }}</li>
                {% endfor %}
            </ul>
        {% endfor %}
    {% endif %}
                            
    """


    sorted_features = list()
    unsorted_features = list()

    character_features = dict()
    # import pdb;pdb.set_trace()
    prestiges = character.char_prestige_classes.all()

    for prestige in prestiges:
        unsorted_features = prestige.features.all()
        sorted_features = sorted(unsorted_features, key=lambda k: k.prereq_class_level)
        character_features[prestige.name] = sorted_features

    return character_features