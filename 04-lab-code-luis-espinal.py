"""
File:  04-Lab-code-luis-espinal-06232022.py
Name: Luis Espinal
Date: 06-23-2022
Purpose: Week 4 Assignment
"""

running = True 
salesTax = .0575
prices = []
while running:
    print("Please enter in at least one item price (or enter q to quit)")
    userResponse = input("Please enter the next price: ")

    if userResponse == "q":
        running = False
    else: 
        price = float(userResponse)
        prices.append(price)
preTaxSum = sum(prices)
salesTaxTotal = round(preTaxSum * salesTax, 2)
roundedPreTaxSum = round(preTaxSum, 2)
postTaxSum = preTaxSum + salesTaxTotal
roundedPostTaxSum = round(postTaxSum, 2)

print("The total amount of all purchases before tax is $",preTaxSum, "and the total sales amount tax is", salesTaxTotal)
print("The total amount of all purchases post tax is $",roundedPostTaxSum)