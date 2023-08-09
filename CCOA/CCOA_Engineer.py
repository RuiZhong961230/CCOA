import os
from copy import deepcopy
import numpy as np
from enoppy.paper_based.pdo_2022 import *


PopSize = 100
DimSize = 10
LB = [-100] * DimSize
UB = [100] * DimSize
TrialRuns = 30
MaxFEs = 20000
MaxIter = int(MaxFEs / PopSize)

curIter = 1

Pop = np.zeros((PopSize, DimSize))
FitPop = np.zeros(PopSize)

Func_num = 0
SuiteName = "Engineer"


# initialize the Pop randomly
def Initialization(func):
    global Pop, FitPop, DimSize
    for i in range(PopSize):
        for j in range(DimSize):
            Pop[i][j] = LB[j] + (UB[j] - LB[j]) * np.random.rand()
        FitPop[i] = func.evaluate(Pop[i])



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
            Off[idx][j] = Pop[idx][j] + np.random.rand() * (X_best[j] - I * Pop[idx][j])   # Eq. (4)
        Off[idx] = np.clip(Off[idx], LB, UB)
        FitOff[idx] = func.evaluate(Off[idx])
        if FitOff[idx] < BestFit:
            BestFit = FitOff[idx]
            X_best = deepcopy(Off[idx])

    for i in range(half, PopSize):
        idx = idx_sort[i]
        r1 = idx_sort[np.random.randint(0, half)]  # A random individual from superior population
        for j in range(DimSize):
            Off[idx][j] = Pop[idx][j] + np.random.rand() * (Pop[idx][j] - Pop[r1][j])   # Simplified Eq. (5)
        Off[idx] = np.clip(Off[idx], LB, UB)
        FitOff[idx] = func.evaluate(Off[idx])

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
            Off[i][j] = Base[j] + np.random.randint(-1, 1) * (LB[j] + np.random.rand() * (UB[j] - LB[j])) / curIter  # Eq. (9)
        Off[i] = np.clip(Off[i], LB, UB)
        FitOff[i] = func.evaluate(Off[i])
        
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
        All_Trial_Best.append(Best_list)
    np.savetxt("./CCOA_Data/Engineer/" + str(Func_num) + ".csv", All_Trial_Best, delimiter=",")


def main():
    global Func_num, DimSize, Pop, MaxFEs, MaxIter, SuiteName, LB, UB

    MaxFEs = 20000
    MaxIter = int(MaxFEs / PopSize)

    Probs = [CSP(), TBTD(), GTD(), TCD(), CBHD(), RCB()]
    Names = ["CSP", "TBTD", "GTD", "TCD", "CBHD", "RCB"]

    for i in range(len(Probs)):
        DimSize = Probs[i].n_dims
        Pop = np.zeros((PopSize, DimSize))
        LB = Probs[i].lb
        UB = Probs[i].ub

        Func_num = Names[i]
        RunCCOA(Probs[i])


if __name__ == "__main__":
    if os.path.exists('./CCOA_Data/Engineer') == False:
        os.makedirs('./CCOA_Data/Engineer')

    main()
