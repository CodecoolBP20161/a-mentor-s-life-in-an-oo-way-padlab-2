from person import Person
import csv
import random


class Mentor(Person):
    def __init__(self, first_name, last_name, year, gender, nickname, slaprate):

        self.nick_name = nickname
        self.slap_rate = int(slaprate)
        super().__init__(first_name, last_name, year, gender)

    def slap(self, students):
        for student in students:
            student.energy_level += 5*self.slap_rate
            print (student.first_name + " slapped!:(")

    def teach(self, students):
        for student in students:
            student.knowledge_level += 10
            student.energy_level -= 5
            print (student.first_name + " got lectured about the current task!")

    @classmethod
    def feedback(cls, cc_class):
        for student in cc_class.students:
            student.energy_level += 15
            print (student.first_name + " you are awesome!")

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
        avg_knowledge = summ_knowledge/len(students)
        dumbies = []
        for student in students:
            if student.knowledge_level < avg_knowledge*0.9:
                dumbies.append(student)
        print ("The following students are a little behind in knowledge, according to the class average:")
        for dumby in dumbies:
            print (dumby.first_name + " " + dumby.last_name)
        return dumbies

    @staticmethod
    def check_energy(students):
        summ_energy = 0
        for student in students:
            summ_energy += student.energy_level
        avg_energy = summ_energy/len(students)
        lazies = []
        for student in students:
            if student.energy_level < avg_energy*0.9:
                lazies.append(student)
        print ("The following students are not energised enough:")
        for lazy in lazies:
            print (lazy.first_name + " " + lazy.last_name)
        return lazies
