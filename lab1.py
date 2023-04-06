#**********************************************************************
# Author:          Michael Davis
# Assignment:      Lab 1
# Date:            April 5, 2023
# Description:     cloning an existing Python program from GitHub
#                  and practicing your debugging skills to find
#                  and fix the errors.
# Input:           floats
# Output:          floats
# Sources:
#*********************************************************************

# Shopping program
# Inputs: float cost, float taxRate, float shipping
# Outputs: float totalPrice

def main():
    taxRate = 0.0
    shipping = 0.0
    totalCost = 0.0

    totalCost = getItemCosts()
    taxRate, shipping = getOtherCosts()
    printReceipt(totalCost, taxRate, shipping)
    # print("\nTax Rate = ", taxRate)             # test print - remove
    # print("\nShipping = ", shipping)            # test print - remove

    print("Thank you!")

# getItemCosts() prompts a user for a list of item
# costs and returns the sum
def getItemCosts():
    itemCost = 0.0
    totalCost = 0.0
    more = 'y'

    while more == 'y':
        itemCost = float(input("Enter item cost $ "))
        # print("\nitemcost = ", itemCost)        # test print - remove
        totalCost = totalCost + itemCost
        # print("\ntotalCost = ", totalCost)      # test print - remove
        more = input("Do you have more items (y/n): ")

    return totalCost
 
# getOtherCosts() prompts a user for the tax rate
# and shipping costs and returns both inputs
def getOtherCosts():
    taxRate = 0.0
    shipping = 0.0

    taxRate = float(input("\nEnter tax rate (i.e. .075 for 7.5%): "))
    shipping = float(input("Enter shipping costs $ "))
    # print("\ntaxRate = ", taxRate)        # test print - remove
    # print("\nshipping = ", shipping)        # test print - remove

    return taxRate, shipping

# printReceipt() accepts total cost, tax rate, and 
# shipping costs and calculates and prints the tax 
# amount, and total cost
def printReceipt(totalCost, taxRate, shipping):
    print("\nSubtotal: $ ", format(totalCost, ".2f"))
    print("Tax: $", format(taxRate * totalCost, ".2f"))
    print("Shipping: $", format(shipping,".2f"))
    print("------------------------")
    print("Please pay: $", format(totalCost + (taxRate * totalCost) + shipping, ".2f"))

main()