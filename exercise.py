import csv

class Exercise():

    def __init__(self, exercise_name, difficulty_level):

        self.exercise_name = exercise_name
        self.difficulty_level = difficulty_level


    @classmethod
    def generate_list(cls, file_name):

        list_of_exercises = []

        with open(file_name) as csvfile:
            all_exercises = csv.reader(csvfile)
            for exercise in all_exercises:
                exercise_object = Exercise(exercise[0], exercise[1])
                list_of_exercises.append(exercise_object)

        return list_of_exercises
