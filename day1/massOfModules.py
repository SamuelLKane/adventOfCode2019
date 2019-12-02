def calculateCostOfWeight(weight):
    return weight // 3 - 2


def recursiveCalculateCostOfFuelWeight(weight):
    cost = calculateCostOfWeight(weight)
    # print(weight, cost)
    if(cost <= 0):
        return 0
    return cost + recursiveCalculateCostOfFuelWeight(cost)


with open("input.data") as fh:
    cost = 0
    for line in fh.readlines():
        cost = cost + recursiveCalculateCostOfFuelWeight(int(line))
    print(cost)
