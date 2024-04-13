from constraint import *


def ml_constraint(*appointments):
    times = []
    for i in appointments:
        times.append(int(i[-2:]))
    return len(times) == len(set(times))


def diff_time(app1, app2):
    sub1, time1 = app1.split("_")
    sub2, time2 = app2.split("_")
    if sub1 == sub2 and abs(int(time1) - int(time2)) <= 1:
        return False
    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = int(input())
    casovi_ML = int(input())
    casovi_R = int(input())
    casovi_BI = int(input())

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Tuka dodadete gi promenlivite--------------------
    AI = []
    for i in range(1, casovi_AI + 1):
        AI.append(f"AI_cas_{i}")
    ML = []
    for i in range(1, casovi_ML + 1):
        ML.append(f"ML_cas_{i}")
    R = []
    for i in range(1, casovi_R + 1):
        R.append(f"R_cas_{i}")
    BI = []
    for i in range(1, casovi_BI + 1):
        BI.append(f"BI_cas_{i}")

    problem.addVariables(AI, AI_predavanja_domain)
    problem.addVariable("AI_vezbi", AI_vezbi_domain)
    problem.addVariables(ML, ML_predavanja_domain)
    problem.addVariable("ML_vezbi", ML_vezbi_domain)
    problem.addVariables(R, R_predavanja_domain)
    problem.addVariables(BI, BI_predavanja_domain)
    problem.addVariable("BI_vezbi", BI_vezbi_domain)
    # ---Tuka dodadete gi ogranichuvanjata----------------

    all_vars = AI + ML + R + BI + ["AI_vezbi", "ML_vezbi", "BI_vezbi"]

    for app1 in all_vars:
        for app2 in all_vars:
            if app1 == app2:
                continue
            problem.addConstraint(diff_time, (app1, app2))

    problem.addConstraint(ml_constraint, ["ML_vezbi"] + ML)

    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)
