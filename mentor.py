from person import Person


class Mentor(Person):
    def __init__(self, first_name, last_name, year, gender, nickname, slaprate):

        self.nickname = nickname
        self.slaprate = slaprate
        super(Mentor, self).__init__(first_name, last_name, year, gender)
