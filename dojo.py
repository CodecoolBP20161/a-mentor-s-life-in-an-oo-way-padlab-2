import random
from exercise import Exercise
import csv

class Dojo(Exercise):

    def __init__(self, exercise_name, difficulty_level):

        super().__init__(exercise_name, difficulty_level)

    def solved(self, student):

        chance_to_solve =float(student.knowledge_level) / (float(self.difficulty_level) + float(student.knowledge_level))
        percent_according_to_knowledge = int(chance_to_solve*100)
        bad_luck_factor = random.randint(1, 100)
        if bad_luck_factor < percent_according_to_knowledge:
            student.energy_level += self.difficulty_level
        else:
            student.energy_level -= 100 - self.difficulty_level
