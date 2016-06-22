import random

class Dojo(Exercise):

    def __init__(self, exercise_name, difficulty_level, ):

        self.exercise_name = exercise_name
        self.difficulty_level = difficulty_level

    def solved(self, student):

        chance_to_solve = (float(self.difficulty_level) + float(student.knowledge_level)) / float(student.knowledge_level)
        percent_according_to_knowledge = int(chance_to_solve*100)
        bad_luck_factor = random.randint(1, 100)
        if bad_luck_factor < percent_according_to_knowledge:
            student.morale += self.difficulty_level
        else:
            student.morale -= 100 - self.difficulty_level