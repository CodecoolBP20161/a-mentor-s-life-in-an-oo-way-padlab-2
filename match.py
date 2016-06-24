import random
import csv


class Match:

    def __init__(self, match_name, important, expectation_probability):
        self.match_name = match_name
        self.important = bool(int(important))
        self.expectation_probability = int(expectation_probability)

    @classmethod
    def generate_list(cls, file_name):
        all_matches = []
        with open("data/" + file_name) as csvfile:
            matches = csv.reader(csvfile)
            for row in matches:
                a_match = Match(row[0], row[1], row[2])
                all_matches.append(a_match)
        return all_matches

    def expected_result(self):
        surprise_rate = random.randit(1, 10)
        if surprise_rate < self.expectation_probability:
            statement = True
        else:
            statement = False
        return statement
