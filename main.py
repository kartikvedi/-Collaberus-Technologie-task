import math


def takingInput():
    list1 = []
    initialSetup = 0
    while True:
        if not initialSetup:
            print("Type 'Exit' to terminate this program")
        input1 = input()
        if input1 == "Exit":
            print("Terminating Program")
            exit()
        input1 = input1.split(" ")
        if not initialSetup:
            if input1[0] != "ALLOT_WATER":
                print("First allot water or Enter in correct format")
                continue
            if int(input1[1]) != 2 and int(input1[1]) != 3:
                print("Only room set available here is of Type '2' or Type '3' ")
                continue
            if ":" not in input1[2]:
                print("Please decide reatio for cooperation water and barrel water")
                continue
            initialSetup = 1
            print("No of guests should be in integer")
        if ("ALLOT_WATER" not in input1) and ("ADD_GUESTS" not in input1) and ("BILL" not in input1):
            print("Enter in correct format")
            continue

        try:
            if input1[0] == "ADD_GUESTS" and not int(input1[1]):
                print("No of guests should be in integer or greater than zero")
                continue
        except:
            print("No of guests should be in integer")
            continue

        if input1[0] == "BILL":
            if len(input1) > 1:
                print("Noother coments with bill")
                continue

        list1.append(input1)
        if "BILL" in input1:
            break

    return list1


def calculateCost(waterUsed, cooperationWater, barrelWater):
    cost1 = waterUsed*(cooperationWater)/(cooperationWater+barrelWater)
    cost1 += math.ceil((waterUsed*(barrelWater) /
                       (cooperationWater+barrelWater)) * 1.5)
    return cost1


def calculateCostforGuest(waterUsedByGuest):
    costOfwater = 0
    costOfwater = waterUsedByGuest*2
    if waterUsedByGuest > 500:
        costOfwater = 1000
        costOfwater += (waterUsedByGuest-500)*3
    if waterUsedByGuest > 1500:
        costOfwater = 4000
        costOfwater += (waterUsedByGuest-1500)*5
    if waterUsedByGuest > 3000:
        costOfwater = 7500
        costOfwater += (waterUsedByGuest-3000)*8
    return costOfwater


def main():
    waterConsumedByOnePerson = 10
    inputs = takingInput()
    typeOfRoom = int(inputs[0][1])
    # print(typeOfRoom)
    waterRatio = inputs[0][2].split(":")
    cooperationWater = waterRatio[0]
    barrelWater = waterRatio[1]

    if typeOfRoom == 3:
        noOfGuests = 5
    elif typeOfRoom == 2:
        noOfGuests = 3
    else:
        print("Wrong type of room")
    print(cooperationWater, barrelWater)
    waterUsed = noOfGuests*30*waterConsumedByOnePerson
    print("waterUsed:", waterUsed)
    initialAmount = calculateCost(
        waterUsed, int(cooperationWater), int(barrelWater))
    print("initialAmount:", initialAmount)
    noOfGuests = 0
    for i in range(1, len(inputs)-1):
        noOfGuests += int(inputs[i][1])
    waterUsedByGuest = noOfGuests*10*30
    guestAmount = calculateCostforGuest(waterUsedByGuest)
    print("guestAmount:", guestAmount)
    totalAmount = guestAmount+initialAmount
    totalWaterUsed = waterUsed+waterUsedByGuest
    print("totalWaterUsed:", totalWaterUsed)
    print("totalAmount:", totalAmount)


if __name__ == "__main__":
    main()