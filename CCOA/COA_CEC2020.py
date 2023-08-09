from mealpy.swarm_based.CoatiOA import OriginalCoatiOA
import os
from opfunu.cec_based import cec2020
import numpy as np
import warnings

warnings.filterwarnings("ignore")


def main(Dim):
    trials = 30
    PopSize = 100
    MaxFEs = 1000 * Dim
    MaxIter = int(MaxFEs / PopSize)

    CEC2020Funcs = [cec2020.F12020(Dim), cec2020.F22020(Dim), cec2020.F32020(Dim), cec2020.F42020(Dim),
                    cec2020.F52020(Dim), cec2020.F62020(Dim), cec2020.F72020(Dim), cec2020.F82020(Dim),
                    cec2020.F92020(Dim), cec2020.F102020(Dim)]

    for i in range(len(CEC2020Funcs)):
        problem_dict = {
            "fit_func": CEC2020Funcs[i].evaluate,
            "lb": [-100] * Dim,
            "ub": [100] * Dim,
            "minmax": "min",
            "log_to": None
        }
        All_Trial_Best = []
        for j in range(trials):
            solver = OriginalCoatiOA(epoch=MaxIter, pop_size=PopSize)
            np.random.seed(2022 + 88 * j)
            best_position, best_fitness_value = solver.solve(problem_dict)
            All_Trial_Best.append(solver.history.list_global_best_fit)
        np.savetxt("./COA_Data/CEC2020/F" + str(i + 1) + "_" + str(Dim) + "D.csv", All_Trial_Best, delimiter=",")


if __name__ == "__main__":
    if os.path.exists('./COA_Data/CEC2020') == False:
        os.makedirs('./COA_Data/CEC2020')
    Dims = [10, 50, 100]
    for Dim in Dims:
        main(Dim)
