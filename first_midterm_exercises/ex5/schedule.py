from constraint import *

def diff_time(app1, appp2):


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = input()
    casovi_ML = input()
    casovi_R = input()
    casovi_BI = input()

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
    for i in casovi_AI:
        AI.append(f"AI_cas_{i}")
    ML = []
    for i in casovi_AI:
        ML.append(f"ML_cas_{i}")
    R = []
    for i in casovi_AI:
        R.append(f"R_cas_{i}")
    BI = []
    for i in casovi_AI:
        BI.append(f"BI_cas_{i}")

    problem.addVariables(AI, AI_predavanja_domain)
    problem.addVariables("AI_vezbi", AI_vezbi_domain)
    problem.addVariables(ML, ML_predavanja_domain)
    problem.addVariables("ML_vezbi", ML_vezbi_domain)
    problem.addVariables(R, R_predavanja_domain)
    problem.addVariables(BI, BI_predavanja_domain)
    problem.addVariables("BI_vezbi", BI_vezbi_domain)
    # ---Tuka dodadete gi ogranichuvanjata----------------



    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)
