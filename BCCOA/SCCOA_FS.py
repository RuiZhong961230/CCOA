import os
from copy import deepcopy
import numpy as np
from mafese import get_dataset
from sklearn.neighbors import KNeighborsClassifier
from numpy.random import seed
from numpy.random import randint
from sklearn.model_selection import cross_val_score


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

Xtrain = None
Ytrain = None

BestFit = 0
BestScale = 0

def Sigmoid(indi):
    new_indi = np.zeros(len(indi))
    for i in range(len(indi)):
        if np.random.rand() >= 1 / (1 + np.exp(-indi[i])):
            new_indi[i] = 1
    return new_indi


def fit_knn(kk):
    global Xtrain, Ytrain, BestFit, BestScale
    new_kk = Sigmoid(kk)
    k = 5
    if len(new_kk) == 0:
        seed(1)
        new_kk = randint(1, np.size(Xtrain, 1))
    sf = []
    for i in range(0, np.size(Xtrain, 1)):
        if new_kk[i] == 1:
            sf.append(i)
    pos = np.transpose(sf)
    if len(pos) == 0:
        return 0
    model = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
    X = Xtrain[:, pos]
    scores = cross_val_score(model, X, Ytrain, cv=5)
    cost = sum(scores) / k
    if cost > BestFit:
        BestFit = cost
        BestScale = sum(new_kk)
    return -cost * 100


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
            Off[idx][j] = Pop[idx][j] + np.random.rand() * (X_best[j] - I * Pop[idx][j])   # Eq. (4)
        Off[idx] = np.clip(Off[idx], LB, UB)
        FitOff[idx] = func(Off[idx])
        if FitOff[idx] < BestFit:
            BestFit = FitOff[idx]
            X_best = deepcopy(Off[idx])

    for i in range(half, PopSize):
        idx = idx_sort[i]
        r1 = idx_sort[np.random.randint(0, half)]  # A random individual from superior population
        for j in range(DimSize):
            Off[idx][j] = Pop[idx][j] + np.random.rand() * (Pop[idx][j] - Pop[r1][j])   # Simplified Eq. (5)
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
            Off[i][j] = Base[j] + np.random.randint(-1, 1) * (LB[j] + np.random.rand() * (UB[j] - LB[j])) / curIter  # Eq. (9)
        Off[i] = np.clip(Off[i], LB, UB)
        FitOff[i] = func(Off[i])
        
    for i in range(PopSize):  # Update
        if FitOff[i] < FitPop[i]:
            FitPop[i] = FitOff[i]
            Pop[i] = deepcopy(Off[i])


def RunCCOA(func):
    global curIter, TrialRuns, Pop, FitPop, DimSize, BestFit, BestScale
    All_Trial_Best = []
    All_Scale = []
    for i in range(TrialRuns):
        Best_list = []
        BestFit = 0
        BestScale = 0
        curIter = 1
        Initialization(func)
        Best_list.append(min(FitPop))
        np.random.seed(2022 + 88 * i)
        while curIter <= MaxIter:
            CCOA(func)
            curIter += 1
            Best_list.append(min(FitPop))
        All_Scale.append(BestScale)
        All_Trial_Best.append(np.abs(Best_list))
    np.savetxt("./SCCOA_Data/FS/Acc/" + Func_num + ".csv", All_Trial_Best, delimiter=",")
    np.savetxt("./SCCOA_Data/FS/Scale/" + Func_num + ".csv", All_Scale, delimiter=",")


def main():
    global Func_num, DimSize, Pop, MaxFEs, MaxIter, LB, UB, Xtrain, Ytrain

    # Datasets = ['BreastCancer', 'BreastEW', 'CongressEW', 'Digits', 'Glass', 'heart', 'HeartEW', 'Hill-valley', 'Horse',
    #             'Ionosphere', 'Madelon', 'Sonar', 'Soybean-small', 'SpectEW', 'WaveformEW', 'wdbc', 'Wine', ]
    Datasets = ['Horse', 'Ionosphere', 'Sonar', 'Soybean-small', 'SpectEW', 'wdbc', 'Wine', ]
    Func_num = 0
    for i in range(len(Datasets)):
        Func_num = Datasets[i]
        dataset = get_dataset(Datasets[i])
        Xtrain, Ytrain = dataset.X, dataset.y
        DimSize = len(Xtrain[0])
        Pop = np.zeros((PopSize, DimSize))
        MaxIter = 5 * DimSize
        LB = [-10] * DimSize
        UB = [10] * DimSize
        RunCCOA(fit_knn)


if __name__ == "__main__":
    if os.path.exists('./SCCOA_Data/FS/Acc') == False:
        os.makedirs('./SCCOA_Data/FS/Acc')
    if os.path.exists('./SCCOA_Data/FS/Scale') == False:
        os.makedirs('./SCCOA_Data/FS/Scale')
    main()
