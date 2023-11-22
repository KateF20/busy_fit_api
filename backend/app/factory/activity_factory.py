from backend.app.enums.activity_enum import ActivityCharacteristics, ActivityCalories, ActivityGroup
from backend.app.entities.Activity import WorkoutActivity, RunningActivity


workout_characteristics = ActivityCharacteristics(
    ActivityCalories.POWER,
    ActivityGroup.POWER
)
running_characteristics = ActivityCharacteristics(
    ActivityCalories.CARDIO,
    ActivityGroup.CARDIO
)


workout = WorkoutActivity(10, workout_characteristics)
running = RunningActivity(15, running_characteristics)
