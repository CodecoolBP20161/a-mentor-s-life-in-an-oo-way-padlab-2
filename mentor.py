from person import Person
from student import Student
from codecool_class import CodecoolClass


class Mentor(Person):
    def __init__(self, first_name, last_name, year, gender, nickname, slaprate):

        self.nick_name = nickname
        self.slap_rate = slaprate
        super(Mentor, self).__init__(first_name, last_name, year, gender)

    def slap(self, student):
        student.energy_level += 5*self.slap_rate

    def teach(self, student):
        student.knowledge_level += 10
        student.energy_level -= 5

    @classmethod
    def feedback(cls, class):
        for student in class.students:
            student.energy_level += 15

    def generate_list(cls, file_name):

        list_of_mentors = []

        with open('data/' + file_name) as csvfile:
            all_mentors = csv.reader(csvfile)
            for mentor in all_mentors:
                mentor_object = Mentor(mentor[0], mentor[1], mentor[2], mentor[3], mentor[4], mentor[5])
                list_of_mentors.append(mentor_object)

        return list_of_mentors
