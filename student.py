from person import Person


class Student(Person):

    def __init__(self, first_name, last_name, year, gender, depend_level, knowledge_level, is_bet_on_expected_result, table_football_level, energy_level):

        super().__init__(first_name, last_name, year, gender)
        self.depend_level = depend_level
        self.knowledge_level = knowledge_level
        self.is_bet_on_expected_result = is_bet_on_expected_result
        self.table_football_level = table_football_level
        self.energy_level = energy_level

    def bet(self, match):
        if match.important = False:
            if self.depend_level == "never" or self.depend_level == "only_interesting":
                if self.is_bet_on_expected_result == was_it_expected:
                    self.energy_level -= 50
                else:
                    self.energy_level += 20
            else:
                if self.is_bet_on_expected_result == was_it_expected:
                    self.energy_level += 50
                else:
                    self.energy_level -= 100

        if match.important = True:
            if self.depend_level == "never":
                if self.is_bet_on_expected_result == was_it_expected:
                    self.energy_level -= 50
                else:
                    self.energy_level += 20
            else:
                if self.is_bet_on_expected_result == was_it_expected:
                    self.energy_level += 50
                else:
                    self.energy_level -= 100
