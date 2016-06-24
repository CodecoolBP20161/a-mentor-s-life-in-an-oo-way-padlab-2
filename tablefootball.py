from mentor import Mentor
from student import Student
from person import Person
import csv
import random


class TableFootballMatch:

    def __init__(self, proper_time, is_official, players):
        self.proper_time = bool(proper_time)
        self.is_official = bool(is_official)
        self.players = int(players)

    @classmethod
    def generate_list(cls, file_name):
        all_matches = []
        with open("data/" + file_name) as csvfile:
            matches = csv.reader(csvfile)
            for row in matches:
                one_match = TableFootballMatch(row[0], row[1], row[2])
                all_matches.append(one_match)
        return all_matches

    def played(self, observed_class):
        teams_list = [[None, None], [None, None]]

        for i in range(0, 2):
            for j in range(0, 2):
                player_found = False
                while not player_found:
                    player_to_check = random.choice(observed_class.students)
                    if player_to_check not in teams_list[0] and player_to_check not in teams_list[1]:
                            teams_list[i][j] = player_to_check
                            player_found = True

        if not self.proper_time:
            mentor_who_acts = random.choice(observed_class.mentors)

            for players in teams_list:
                mentor_who_acts.slap(players)

        else:
            score = []
            for team in range(0, 2):
                point = teams_list[team][0].table_football_level + teams_list[team][1].table_football_level
                score.append(point)

            if self.is_official:
                moral_booster = 200
            else:
                moral_booster = 100

            if score[0] > score[1]:
                teams_list[0][0].energy_level += moral_booster
                teams_list[0][1].energy_level += moral_booster
                teams_list[1][0].energy_level -= moral_booster
                teams_list[1][1].energy_level -= moral_booster
            else:
                teams_list[1][0].energy_level += moral_booster
                teams_list[1][1].energy_level += moral_booster
                teams_list[0][0].energy_level -= moral_booster
                teams_list[0][1].energy_level -= moral_booster
