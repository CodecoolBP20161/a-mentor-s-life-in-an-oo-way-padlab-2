from exercise import Exercise
import csv

class Project(Exercise):

    def __init__(self, exercise_name, difficulty_level, ):

        super().__init__(exercise_name, difficulty_level)

    def worked_on(self):
        pass
