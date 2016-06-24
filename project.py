from exercise import Exercise
import csv


class Project(Exercise):

    def __init__(self, exercise_name, difficulty_level, ):

        super().__init__(exercise_name, difficulty_level)

    def worked_on(self, list_of_students):
        sum_knowledge_level = 0
        for student in list_of_students:
            sum_knowledge_level += student.knowledge_level
        ratio = 1 + self.difficulty_level/(sum_knowledge_level/len(list_of_students))

        for student in list_of_students:
            student.knowledge_level = student.knowledge_level * ratio
