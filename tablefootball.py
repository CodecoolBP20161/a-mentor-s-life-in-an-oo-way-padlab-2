from mentor import Mentor
from student import Student
from person import Person


class TableFootballMatch:

    def __init__(self, proper_time, is_official, players):
        self.proper_time = proper_time
        self.is_official = is_official
        self.players = players


    @classmethod
    def generate_list(cls, file_name):
        all_matches = []
        with open("data/" + file_name) as csvfile:
            matches = csv.reader(csvfile)
            for row in matches:
                one_match = TableFootballMatch(row[0], row[1], row[2])
                all_matches.append(one_match)
        return all_matches

    def played(self):
        teams_list = [[0, 0], [0, 0]]

        for team in teams_list:
            for player in team:
                player_found = False
                while not player_found:
                    player_to_check = random.choice(codecool_bp.students)
                    if player_to_check not in teams_list[0] and player_to_check not in team[1]:
                        player = player_to_check
                        player_found = True

        if self.proper_time == False:
            mentor_who_acts = random.choice(codecool_bp.mentors)

            for players in teams_list:
                for player in players:
                    mentor_who_acts.slap(player)

        else:
            score = []
            for team in range(0, 2):
                point = teams_list[team][0].table_football_level + teams_list[team][1].table_football_level
                score.append(point)

            if self.is_official == True:
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
