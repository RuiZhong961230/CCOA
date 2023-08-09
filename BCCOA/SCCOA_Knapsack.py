import os
from copy import deepcopy
import numpy as np
from Discrete.knapsack1 import *
from Discrete.knapsack2 import *

PopSize = 20
DimSize = 10
LB = [-10] * DimSize
UB = [10] * DimSize
TrialRuns = 30
MaxIter = 5 * DimSize

curIter = 1

Pop = np.zeros((PopSize, DimSize))
FitPop = np.zeros(PopSize)

Func_num = 0
Prob = None


def Sigmoid(indi):
    new_indi = np.zeros(len(indi))
    for i in range(len(indi)):
        if np.random.rand() >= 1 / (1 + np.exp(-indi[i])):
            new_indi[i] = 1
    return new_indi


def Fitness(indi):
    global Prob
    solution = Sigmoid(indi)
    return -Prob(solution)


# initialize the Pop randomly
def Initialization(func):
    global Pop, FitPop, DimSize
    for i in range(PopSize):
        for j in range(DimSize):
            Pop[i][j] = LB[j] + (UB[j] - LB[j]) * np.random.rand()
        FitPop[i] = func(Pop[i])


def CCOA(func):
    global Pop, FitPop, PopSize, DimSize
    Exploration(func)
    Exploitation(func)


def Exploration(func):
    global Pop, FitPop, PopSize, DimSize, LB, UB

    idx_sort = np.argsort(FitPop)
    X_best = Pop[idx_sort[0]]
    BestFit = FitPop[idx_sort[0]]
    Off = np.zeros((PopSize, DimSize))
    FitOff = np.zeros(PopSize)

    half = int(PopSize / 2)
    for i in range(half):
        idx = idx_sort[i]
        I = np.random.randint(1, 3)
        for j in range(DimSize):
            Off[idx][j] = Pop[idx][j] + np.random.rand() * (X_best[j] - I * Pop[idx][j])  # Eq. (4)
        Off[idx] = np.clip(Off[idx], LB, UB)
        FitOff[idx] = func(Off[idx])
        if FitOff[idx] < BestFit:
            BestFit = FitOff[idx]
            X_best = deepcopy(Off[idx])

    for i in range(half, PopSize):
        idx = idx_sort[i]
        r1 = idx_sort[np.random.randint(0, half)]  # A random individual from superior population
        for j in range(DimSize):
            Off[idx][j] = Pop[idx][j] + np.random.rand() * (Pop[idx][j] - Pop[r1][j])  # Simplified Eq. (5)
        Off[idx] = np.clip(Off[idx], LB, UB)
        FitOff[idx] = func(Off[idx])

    for i in range(PopSize):  # Update
        if FitOff[i] < FitPop[i]:
            FitPop[i] = FitOff[i]
            Pop[i] = deepcopy(Off[i])


def Exploitation(func):
    global curIter, Pop, FitPop, PopSize, DimSize, LB, UB
    Off = np.zeros((PopSize, DimSize))
    FitOff = np.zeros(PopSize)
    idx_sort = np.argsort(FitPop)

    for i in range(PopSize):
        Candidate = [Pop[idx_sort[0]], Pop[idx_sort[1]], Pop[idx_sort[2]], Pop[i]]
        Base = Candidate[np.random.randint(0, len(Candidate))]
        for j in range(DimSize):
            Off[i][j] = Base[j] + np.random.randint(-1, 1) * (
                        LB[j] + np.random.rand() * (UB[j] - LB[j])) / curIter  # Eq. (9)
        Off[i] = np.clip(Off[i], LB, UB)
        FitOff[i] = func(Off[i])

    for i in range(PopSize):  # Update
        if FitOff[i] < FitPop[i]:
            FitPop[i] = FitOff[i]
            Pop[i] = deepcopy(Off[i])


def RunCCOA(func):
    global curIter, TrialRuns, Pop, FitPop, DimSize
    All_Trial_Best = []
    for i in range(TrialRuns):
        Best_list = []
        curIter = 1
        Initialization(func)
        Best_list.append(min(FitPop))
        np.random.seed(2022 + 88 * i)
        while curIter <= MaxIter:
            CCOA(func)
            curIter += 1
            Best_list.append(min(FitPop))
        All_Trial_Best.append(np.abs(Best_list))
    np.savetxt("./SCCOA_Data/Knapsack/" + Func_num + ".csv", All_Trial_Best, delimiter=",")


def main():
    global Func_num, DimSize, Pop, MaxIter, LB, UB, Prob

    Probs = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, p1, p2, p3, p4, p5, p6, p7, p8]
    Names = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"]
    Dims = [10, 20, 4, 4, 15, 10, 7, 23, 5, 20, 10, 5, 6, 7, 8, 7, 15, 24]
    Func_num = 0
    for i in range(len(Probs)):
        Prob = Probs[i]
        Func_num = Names[i]
        DimSize = Dims[i]
        Pop = np.zeros((PopSize, DimSize))
        MaxIter = 5 * DimSize
        LB = [-10] * DimSize
        UB = [10] * DimSize
        RunCCOA(Fitness)


if __name__ == "__main__":
    if os.path.exists('./SCCOA_Data/Knapsack') == False:
        os.makedirs('./SCCOA_Data/Knapsack')
    main()
