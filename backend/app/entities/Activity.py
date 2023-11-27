class Activity:
    def __init__(self, duration, characteristics):
        self.__name = 'Default Activity'
        self.__group = characteristics.group
        self.__duration = duration  # in minutes
        self.__calories_per_minute = characteristics.calories

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def duration(self):
        return self.__duration

    @property
    def calories_per_minute(self):
        return self.__calories_per_minute

    @calories_per_minute.setter
    def calories_per_minute(self, calories):
        self.__calories_per_minute = calories

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group):
        self.__group = group

    def calculate_calories(self):
        return self.duration * self.calories_per_minute

    def __str__(self):
        return self.__class__.__name__


class WorkoutActivity(Activity):
    def __init__(self, duration, characteristics):
        super().__init__(duration, characteristics)
        self.name = 'Workout'


class RunningActivity(Activity):
    def __init__(self, duration, characteristics):
        super().__init__(duration, characteristics)
        self.name = 'Running'
