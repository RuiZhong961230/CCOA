"""
  Datasets from: https://www.sciencedirect.com/science/article/pii/S1568494614000799
  Bhattacharjee, K.K., Sarmah, S.P.: Shuffled frog leaping algorithm and its application to 0/1 knapsack problem.
  Applied Soft Computing 19, 252–263 (2014)
"""


def f1(indi):
    """
    :param indi: Dim = 10
    :return:
    """
    if len(indi) != 10:
        print("The input for f1 is invalid")
        return
    w = [95, 4, 60, 32, 23, 72, 80, 62, 65, 46]
    p = [55, 10, 47, 5, 4, 50, 8, 61, 85, 87]
    b = 269
    price = 0
    weight = 0
    for i in range(len(indi)):
        if indi[i] == 1:
            price += p[i]
            weight += w[i]
    if weight > b:
        price = -1
    return price


def f2(indi):
    """
    :param indi: Dim = 20
    :return:
    """
    if len(indi) != 20:
        print("The input for f2 is invalid")
        return
    w = [92, 4, 43, 83, 84, 68, 92, 82, 6, 44, 32, 18, 56, 83, 25, 96, 70, 48, 14, 58]
    p = [44, 46, 90, 72, 91, 40, 75, 35, 8, 54, 78, 40, 77, 15, 61, 17, 75, 29, 75, 63]
    b = 878
    price = 0
    weight = 0
    for i in range(len(indi)):
        if indi[i] == 1:
            price += p[i]
            weight += w[i]
    if weight > b:
        price = -1
    return price


def f3(indi):
    """
    :param indi: Dim = 4
    :return:
    """
    if len(indi) != 4:
        print("The input for f3 is invalid")
        return
    w = [6, 5, 9, 7]
    p = [9, 11, 13, 15]
    b = 20
    price = 0
    weight = 0
    for i in range(len(indi)):
        if indi[i] == 1:
            price += p[i]
            weight += w[i]
    if weight > b:
        price = -1
    return price


def f4(indi):
    """
    :param indi: Dim = 4
    :return:
    """
    if len(indi) != 4:
        print("The input for f4 is invalid")
        return
    w = [2, 4, 6, 7]
    p = [6, 10, 12, 13]
    b = 11
    price = 0
    weight = 0
    for i in range(len(indi)):
        if indi[i] == 1:
            price += p[i]
            weight += w[i]
    if weight > b:
        price = -1
    return price


def f5(indi):
    """
    :param indi: Dim = 15
    :return:
    """
    if len(indi) != 15:
        print("The input for f5 is invalid")
        return
    w = [56.358531, 80.87405, 47.987304, 89.59624, 74.660482, 85.894345, 51.353496,
         1.498459, 36.445204, 16.589862, 44.569231, 0.466933, 37.788018, 57.118442,
         60.716575]
    p = [0.125126, 19.330424, 58.500931, 35.029145, 82.284005, 17.41081, 71.050142,
         30.399487, 9.140294, 14.731285, 98.852504, 11.908322, 0.89114,
         53.166295, 60.176397]
    b = 375
    price = 0
    weight = 0
    for i in range(len(indi)):
        if indi[i] == 1:
            price += p[i]
            weight += w[i]
    if weight > b:
        price = -1
    return price


def f6(indi):
    """
    :param indi: Dim = 10
    :return:
    """
    if len(indi) != 10:
        print("The input for f6 is invalid")
        return
    w = [30, 25, 20, 18, 17, 11, 5, 2, 1, 1]
    p = [20, 18, 17, 15, 15, 10, 5, 3, 1, 1]
    b = 60

    price = 0
    weight = 0
    for i in range(len(indi)):
        if indi[i] == 1:
            price += p[i]
            weight += w[i]
    if weight > b:
        price = -1
    return price


def f7(indi):
    """
    :param indi: Dim = 7
    :return:
    """
    if len(indi) != 7:
        print("The input for f7 is invalid")
        return
    w = [31, 10, 20, 19, 4, 3, 6]
    p = [70, 20, 39, 37, 7, 5, 10]
    b = 50
    price = 0
    weight = 0
    for i in range(len(indi)):
        if indi[i] == 1:
            price += p[i]
            weight += w[i]
    if weight > b:
        price = -1
    return price


def f8(indi):
    """
    :param indi: Dim = 23
    :return:
    """
    if len(indi) != 23:
        print("The input for f8 is invalid")
        return
    w = [983, 982, 981, 980, 979, 978, 488, 976, 972, 486, 486, 972,
         972, 485, 485, 969, 966, 483, 964, 963, 961, 958, 959]
    p = [81, 980, 979, 978, 977, 976, 487, 974, 970, 485, 485, 970,
         970, 484, 484, 976, 974, 482, 962, 961, 959, 958, 857]
    b = 10000
    price = 0
    weight = 0
    for i in range(len(indi)):
        if indi[i] == 1:
            price += p[i]
            weight += w[i]
    if weight > b:
        price = -1
    return price


def f9(indi):
    """
    :param indi: Dim = 5
    :return:
    """
    if len(indi) != 5:
        print("The input for f9 is invalid")
        return
    w = [15, 20, 17, 8, 31]
    p = [33, 24, 36, 37, 12]
    b = 80
    price = 0
    weight = 0
    for i in range(len(indi)):
        if indi[i] == 1:
            price += p[i]
            weight += w[i]
    if weight > b:
        price = -1
    return price


def f10(indi):
    """
    :param indi: Dim = 20
    :return:
    """
    if len(indi) != 20:
        print("The input for f10 is invalid")
        return
    w = [84, 83, 43, 4, 44, 6, 82, 92, 25, 83,
         56, 18, 58, 14, 48, 70, 96, 32, 68, 92]
    p = [91, 72, 90, 46, 55, 8, 35, 75, 61, 15,
         77, 40, 63, 75, 29, 75, 17, 78, 40, 44]
    b = 879
    price = 0
    weight = 0
    for i in range(len(indi)):
        if indi[i] == 1:
            price += p[i]
            weight += w[i]
    if weight > b:
        price = -1
    return price

