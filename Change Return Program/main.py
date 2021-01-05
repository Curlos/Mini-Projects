def changeReturn(cost, moneyGiven):
    QUARTER = 0.25
    DIME = 0.10
    NICKEL = 0.05
    PENNY = 0.01

    if(moneyGiven < cost):
        return "Not enough money!"
    elif(moneyGiven == cost):
        return "No change returned."
    elif(moneyGiven > cost):
        change = {"quarters": 0, "dimes": 0, "nickels": 0, "pennies": 0}

        while(True):
            if(round(moneyGiven, 2) == 0):
                break

            if(round(moneyGiven, 2) - QUARTER >= 0):
                moneyGiven -= QUARTER
                change["quarters"] += 1
            elif(round(moneyGiven, 2) - DIME >= 0):
                moneyGiven -= DIME
                change["dimes"] += 1
            elif(round(moneyGiven, 2) - NICKEL >= 0):
                moneyGiven -= NICKEL
                change["nickels"] += 1
            elif(round(moneyGiven, 2) - PENNY >= 0):
                moneyGiven -= PENNY
                change["pennies"] += 1
        return change


print(changeReturn(19.99, 25.98))
