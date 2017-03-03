"""
# TODO:  Need to create a set of classes and functions to run a character sheet in 5th ed DnD.
# TODO:  Would be nice to have spell interaction.
# TODO:  Will need to have persistence.
# TODO:  Should include a dice roller and display rolls as well as bonuses.



Expected Data Structures:
name = string
race = string
char_class = {class_name: level, class_name: level, etc.}
prof = int
ability_scores = {'STR': int, 'DEX': int, etc.}
saving_throws = {'STR': (int, bool), etc.}
skills = {'acrobatics': (int, bool, 'DEX'), etc.}
"""


from math import ceil



class Character:
    """
    Holds data from the player sheet.
    """

    def __init__(self, name, race, char_class, ability_scores, saving_throws, skills):
        self.char_name = name
        self.char_race = race
        self.char_class = char_class
        self.ability_scores = ability_scores
        self.saving_throws = saving_throws
        self.skills = skills
        self.char_level = self.get_level()
        self.char_prof = self.get_prof()

    def get_ability_score(self, ability):
        """
        Returns the ability score itself (eg. 10 or 19)
        """

        return self.ability_scores[ability]

    def get_ability_bonus(self, ability):
        """returns the bonus for the ability score as int"""

        return (self.ability_scores[ability] - 10) // 2

    def get_savings_throw(self, ability):
        """return the savings throw bonus as an int"""

        score = 0
        score += self.get_ability_bonus(ability)
        if saving_throws[ability]:
            score += self.char_prof

        return score

    def get_savings_prof(self, ability):
        """returns the a boolean if proficient or not"""

        return self.saving_throws[ability]

    def get_skill_bonus(self, skill):
        """returns skill bonus as int"""

        score = 0
        score += self.skills[skill][0] * self.char_prof
        score += self.get_ability_bonus(self.skills[skill][1])
        score += int(self.skills[skill][2] * self.char_prof)

        return score

    def get_skill_prof(self, skill):
        """returns proficiency as bool"""

        return self.skills[skill][0]

    def get_skill_ability(self, skill):
        """returns the ability for skill as a string"""

        return self.skills[skill][1]

    def get_level(self):
        """returns character level as int"""

        level = 0

        for class_level in self.char_class.values():
            level += class_level

        return level

    def get_prof(self):
        """
        Returns the proficiency bonus as int.
        """

        return int(ceil(self.char_level / 4) + 1)

    def __str__(self):
        return "This is {0.char_name}. They are a {0.char_race}. Their level is {0.char_level}.".format(self)


if __name__ == '__main__':

    name = 'Aesier Take Two!'
    race = 'Half-Elf'
    char_class = {'Sorc': 8, 'Bard': 3}

    ability_scores = {'STR': 8, 'DEX': 16, 'CON': 14, 'INT': 8, 'WIS': 12, 'CHA': 19}

    saving_throws = {'STR': False, 'DEX': True, 'CON': True, 'INT': False, 'WIS': False, 'CHA': True}

    skills = {'acrobatics': (True, 'DEX', 1), 'animal_handling': (False, 'WIS', .5), 'arcana': (True, 'INT', 0),
              'athletics': (False, 'STR', .5), 'deception': (True, 'CHA', 0), 'history': (False, 'INT', .5),
              'insight': (True, 'WIS', 0), 'intimidation': (False, 'CHA', .5), 'investigation': (True, 'INT', 0),
              'medicine': (True, 'WIS', 0), 'nature': (False, 'INT', .5), 'perception': (True, 'WIS', 1),
              'performance': (False, 'CHA', .5), 'persuasion': (True, 'CHA', 0), 'religion': (False, 'INT', .5),
              'sleight_of_hand': (True, 'DEX', 0), 'stealth': (True, 'DEX', 0), 'survival': (False, 'WIS', .5)}


    test = Character(name, race, char_class, ability_scores, saving_throws, skills)


    print("Name: {}".format(test.char_name))
    print("Race: {}".format(test.char_race))
    print("Level: {}".format(test.char_level))
    print("Classes: {}".format(test.char_class))
    print("Proficiency: {}".format(test.char_prof))
    print()
    print("STR Score: {}".format(test.get_ability_score('STR')))
    print("STR Bonus: {}".format(test.get_ability_bonus('STR')))
    print()
    print("STR STh: {}".format(test.get_savings_throw('STR')))
    print("CON STh Prof: {}".format(test.get_savings_prof('CON')))
    print()
    print("Acrobatics Score: {}".format(test.get_skill_bonus('acrobatics')))
    print("Religion Prof: {}".format(test.get_skill_prof('religion')))
    print("Investigation Ability Score: {}".format(test.get_skill_ability('investigation')))
    print()
    print(test)












# sadf
