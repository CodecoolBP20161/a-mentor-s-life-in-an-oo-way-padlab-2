from person import Person
import csv


class Student(Person):

    def __init__(self, first_name, last_name, year, gender, depend_level, knowledge_level,
                 is_bet_on_expected_result, table_football_level, energy_level):

        super().__init__(first_name, last_name, year, gender)
        self.depend_level = depend_level
        self.knowledge_level = int(knowledge_level)
        self.is_bet_on_expected_result = bool(int(is_bet_on_expected_result))
        self.table_football_level = int(table_football_level)
        self.energy_level = int(energy_level)

    def bet(self, match, was_it_expected):
        if not match.important:
            if self.depend_level == "never" or self.depend_level == "only_interesting":
                if self.is_bet_on_expected_result == was_it_expected:
                    self.energy_level -= 50
                    next_line = input(self.first_name + " is sad, because " + self.gender + " did not play, even tough " + self.gender + " knew the score.")
                else:
                    self.energy_level += 20
                    next_line = input(self.first_name + " is happy, because " + self.gender + " did not play, and " + self.gender + " had no idea whatsoever what was gonna happen on the match.")

            else:
                if self.is_bet_on_expected_result == was_it_expected:
                    self.energy_level += 50
                    next_line = input(self.first_name + " is happy, because " + self.gender + " won a lot of money.")
                else:
                    self.energy_level -= 100
                    next_line = input(self.first_name + " is sad, because " + self.gender + " lost a lot of money")

        if match.important:
            if self.depend_level == "never":
                if self.is_bet_on_expected_result == was_it_expected:
                    self.energy_level -= 50
                    next_line = input(self.first_name + " is sad, because " + self.gender + " did not play, even tough " + self.gender + " knew the score.")
                else:
                    self.energy_level += 20
                    next_line = input(self.first_name + " is happy, because " + self.gender + " did not play, and " + self.gender + " had no idea whatsoever what was gonna happen on the match.")
            else:
                if self.is_bet_on_expected_result == was_it_expected:
                    self.energy_level += 50
                    next_line = input(self.first_name + " is happy, because " + self.gender + " won a lot of money.")
                else:
                    self.energy_level -= 100
                    next_line = input(self.first_name + " is sad, because " + self.gender + " lost a lot of money")

    @classmethod
    def generate_list(cls, file_name):

        list_of_students = []

        with open('data/' + file_name) as csvfile:
            all_students = csv.reader(csvfile)
            for student in all_students:
                student_object = Student(student[0], student[1], student[2], student[3], student[4], student[5],
                                         student[6], student[7], student[8])
                list_of_students.append(student_object)

        return list_of_students
