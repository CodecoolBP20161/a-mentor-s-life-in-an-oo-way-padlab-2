from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from match import Match
from tablefootball import TableFootballMatch
from dojo import Dojo
from project import Project
import csv
import random

codecool_bp = CodecoolClass.generate_local()

# for random:
observed_class = codecool_bp
all_students = codecool_bp.students
all_mentors = codecool_bp.mentors
all_matches = Match.generate_list('matches.csv')
table_football_matches = TableFootballMatch.generate_list('tablefootball.csv')
all_dojos = Dojo.generate_list('dojos.csv')
all_projects = Project.generate_list('projects.csv')

days_of_the_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')

# One week
for day in days_of_the_week:

    # One day
    match_of_yesterday = random.choice(all_matches)
    was_it_expected = match_of_yesterday.expected_result
    for student in all_students:
        student.bet(match_of_yesterday, was_it_expected)
    for student in all_students:
        dojo_to_solve = random.choice(all_dojos)
        dojo_to_solve.solved(student)
    for events in range(3):
        played_table_football_match = random.choice(table_football_matches)
        played_table_football_match.played(observed_class)
        actual_project = random.choice(all_projects)
        actual_project.worked_on()
    Mentor.feedback(observed_class)
