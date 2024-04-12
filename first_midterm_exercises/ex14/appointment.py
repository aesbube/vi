import constraint
from constraint import *


def simona_constraint(simona, marija, petar):
    return simona + marija + petar >= 2


def appointment_constraint(simona, marija, petar, time):
    if simona == 0: return False
    simona_free = (13, 14, 16, 19)
    marija_free = (14, 15, 18)
    petar_free = (12, 13, 16, 17, 18, 19)
    people = []
    if simona == 1: people.append(simona_free)
    if marija == 1: people.append(marija_free)
    if petar == 1: people.append(petar_free)

    valid = 0
    for person in people:
        if time in person:
            valid += 1

    return valid == len(people)


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Simona_prisustvo", [0, 1])
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", range(12, 20))
    # ----------------------------------------------------

    problem.addConstraint(simona_constraint, ["Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo"])
    problem.addConstraint(appointment_constraint,
                          ["Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo", "vreme_sostanok"])
    # ----------------------------------------------------

    solutions = problem.getSolutions()

    for solution in solutions:
        reordered_solution = {'Simona_prisustvo': solution['Simona_prisustvo'],
                              'Marija_prisustvo': solution['Marija_prisustvo'],
                              'Petar_prisustvo': solution['Petar_prisustvo'],
                              'vreme_sostanok': solution['vreme_sostanok']}
        print(reordered_solution)

# :)