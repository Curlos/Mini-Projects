def calculateTax(cost, taxRatePercentage):
    ''' Asks the user to enter a cost and either a country or state tax. It then returns the tax plus the total cost with tax. '''
    tax = taxRatePercentage / 100
    totalTax = tax * cost
    totalCostAfterTax = cost + totalTax
    return {"Total tax": round(totalTax, 2), "Total cost": round(totalCostAfterTax, 2)}


print(calculateTax(100, 6))
print(calculateTax(100, 6)["Total tax"])
print(calculateTax(100, 6)["Total cost"])
