"""
  Datasets from: https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html
"""


def p1(indi):
    """
    :param indi: Dim = 10
    :return:
    """
    if len(indi) != 10:
        print("The input for p1 is invalid")
        return
    w = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
    p = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
    b = 165
    price = 0
    weight = 0
    for i in range(len(indi)):
        if indi[i] == 1:
            price += p[i]
            weight += w[i]
    if weight > b:
        price = -1
    return price


def p2(indi):
    """
    :param indi: Dim = 5
    :return:
    """
    if len(indi) != 5:
        print("The input for p2 is invalid")
        return
    w = [12, 7, 11, 8, 9]
    p = [24, 13, 23, 15, 16]
    b = 26
    price = 0
    weight = 0
    for i in range(len(indi)):
        if indi[i] == 1:
            price += p[i]
            weight += w[i]
    if weight > b:
        price = -1
    return price


def p3(indi):
    """
    :param indi: Dim = 6
    :return:
    """
    if len(indi) != 6:
        print("The input for p3 is invalid")
        return
    w = [56, 59, 80, 64, 75, 17]
    p = [50, 50, 64, 46, 50, 5]
    b = 190
    price = 0
    weight = 0
    for i in range(len(indi)):
        if indi[i] == 1:
            price += p[i]
            weight += w[i]
    if weight > b:
        price = -1
    return price


def p4(indi):
    """
    :param indi: Dim = 7
    :return:
    """
    if len(indi) != 7:
        print("The input for p4 is invalid")
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


def p5(indi):
    """
    :param indi: Dim = 8
    :return:
    """
    if len(indi) != 8:
        print("The input for p5 is invalid")
        return
    w = [25, 35, 45, 5, 25, 3, 2, 2]
    p = [350, 400, 450, 20, 70, 8, 5, 5]
    b = 104
    price = 0
    weight = 0
    for i in range(len(indi)):
        if indi[i] == 1:
            price += p[i]
            weight += w[i]
    if weight > b:
        price = -1
    return price


def p6(indi):
    """
    :param indi: Dim = 7
    :return:
    """
    if len(indi) != 7:
        print("The input for p6 is invalid")
        return
    w = [41, 50, 49, 59, 55, 57, 60]
    p = [442, 525, 511, 593, 546, 564, 617]
    b = 169
    price = 0
    weight = 0
    for i in range(len(indi)):
        if indi[i] == 1:
            price += p[i]
            weight += w[i]
    if weight > b:
        price = -1
    return price


def p7(indi):
    """
    :param indi: Dim = 15
    :return:
    """
    if len(indi) != 15:
        print("The input for p7 is invalid")
        return
    w = [70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120]
    p = [135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240]
    b = 750
    price = 0
    weight = 0
    for i in range(len(indi)):
        if indi[i] == 1:
            price += p[i]
            weight += w[i]
    if weight > b:
        price = -1
    return price


def p8(indi):
    """
    :param indi: Dim = 24
    :return:
    """
    if len(indi) != 24:
        print("The input for p8 is invalid")
        return
    w = [382745, 799601, 909247, 729069, 467902, 44328, 34610, 698150, 823460, 903959, 853665, 551830, 610856, 670702, 488960, 951111, 323046, 446298, 931161, 31385, 496951, 264724, 224916, 169684]
    p = [825594, 1677009, 1676628, 1523970, 943972, 97426, 69666, 1296457, 1679693, 1902996, 1844992, 1049289, 1252836, 1319836, 953277, 2067538, 675367, 853655, 1826027, 65731, 901489, 577243, 466257, 369261]
    b = 6404180
    price = 0
    weight = 0
    for i in range(len(indi)):
        if indi[i] == 1:
            price += p[i]
            weight += w[i]
    if weight > b:
        price = -1
    return price
