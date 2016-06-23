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
