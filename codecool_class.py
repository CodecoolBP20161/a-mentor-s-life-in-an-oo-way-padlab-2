from mentor import Mentor
from student import Student


class CodecoolClass:
    def __init__(self, location, year, mentors_csv, students_csv):
        self.location = location
        self.year = year
        self.mentors = Mentor.generate_list(mentors_csv)
        self.students = Student.generate_list(students_csv)

    def find_student_by_full_name(self, fullname):
        for student in self.students:
            if student[0] == fullname.split(' ')[0] and student[1] == fullname.split(' ')[1]:
                return student
        raise ValueError("No student found by the given name")

    def find_mentor_by_full_name(self, fullname):
        for mentor in self.mentors:
            if mentor[0] == fullname.split(' ')[0] and mentor[1] == fullname.split(' ')[1]:
                return mentor
        raise ValueError("No mentor found by the given name")

    @classmethod
    def generate_local(cls):
        return CodecoolClass("Budapest", 2016, "/data/mentors.csv", "/data/students.csv")
