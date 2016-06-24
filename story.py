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
    next_line = input("\nIt's " + day + ".\n")
    match_of_yesterday = random.choice(all_matches)
    was_it_expected = bool(match_of_yesterday.expected_result)
    print("Yesterday there was a match: " + match_of_yesterday.match_name)
    if match_of_yesterday.important == True:
        next_line = input("It was a really interesting match, a lot of students placed a bet on it.\n")
    else:
        next_line = input("Only the addicted players placed a bet on that.\n")
    for student in all_students:
        student.bet(match_of_yesterday, was_it_expected)
    next_line = input("\nA few students seems to have a bad day...")
    random.choice(all_mentors).slap(Mentor.check_energy(all_students))
    next_line = input("They deserved it.\n")
    for student in all_students:
        dojo_to_solve = random.choice(all_dojos)
        dojo_to_solve.solved(student)
    next_line = input("\nSome students are so heavily affected by their lack of knowledge... and the hard time for them is just coming...")
    random.choice(all_mentors).slap(Mentor.check_energy(all_students))
    next_line = input("Probably, they feel much better now.\n")
    for events in range(3):
        played_table_football_match = random.choice(table_football_matches)
        played_table_football_match.played(observed_class)
        actual_project = random.choice(all_projects)
        actual_project.worked_on(all_students)
    random.choice(all_mentors).teach(Mentor.check_knowledge(all_students))
    if day != 'Friday':
        next_line = input("The day is over. A lot of students bet on the match of the day.")
    else:
        next_line = input("\nIt is feedback time!!!")
        Mentor.feedback(observed_class)
        print("\nThe week is over.")
