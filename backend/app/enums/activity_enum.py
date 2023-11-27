from enum import IntEnum, Flag


class ActivityGroup(Flag):
    DEFAULT = 'Default group'
    CARDIO = 'Cardio'
    POWER = 'Power'
    FLEXIBILITY = 'Flexibility'


class ActivityCalories(IntEnum):
    DEFAULT = 0
    CARDIO = 20
    POWER = 10
    FLEXIBILITY = 5


class ActivityCharacteristics:
    def __init__(self, calories, group):
        self.__calories = calories
        self.__group = group

    @property
    def calories(self):
        return self.__calories

    @property
    def group(self):
        return self.__group
