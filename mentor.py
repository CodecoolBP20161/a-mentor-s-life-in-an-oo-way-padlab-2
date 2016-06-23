from person import Person
import csv


class Mentor(Person):
    def __init__(self, first_name, last_name, year, gender, nickname, slaprate):

        self.nick_name = nickname
        self.slap_rate = slaprate
        super().__init__(first_name, last_name, year, gender)

    def slap(self, student):
        student.energy_level += 5*self.slap_rate

    def teach(self, student):
        student.knowledge_level += 10
        student.energy_level -= 5

    @classmethod
    def feedback(cls, a):
        for student in a.students:
            student.energy_level += 15

    @classmethod
    def generate_list(cls, file_name):

        list_of_mentors = []

        with open('data/' + file_name) as csvfile:
            all_mentors = csv.reader(csvfile)
            for mentor in all_mentors:
                mentor_object = Mentor(mentor[0], mentor[1], mentor[2], mentor[3], mentor[4], mentor[5])
                list_of_mentors.append(mentor_object)

        return list_of_mentors

    @staticmethod
    def check_knowledge(students):
        summ_knowledge = 0
        for student in students:
            summ_knowledge += student.knowledge_level
        avg_knowledge = summ_knowledge/students.length()
        dumbies = []
        for student in students:
            if student.knowledge_level < avg_knowledge*0.9:
                dumbies.append(student)
        return dumbies

    @staticmethod
    def check_energy(students):
        summ_energy = 0
        for student in students:
            summ_energy += student.energy_level
        avg_energy = summ_energy/students.length()
        lazies = []
        for student in students:
            if student.energy_level < avg_energy*0.9:
                lazies.append(student)
        return lazies
