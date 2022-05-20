#!/usr/bin/python

money = eval(input("Enter an amount of money: "))
dollars = int(money)
#round fixes rounding error
#test 55.01 without the round
remainder = round((money - dollars),2)

quarters = int((remainder)/.25)
remainder = remainder - (quarters*.25)

dimes = int((money - dollars - quarters*.25)/.1)
remainder = remainder - (dimes*.1)

nickels = int((remainder)/.05)
remainder = remainder - (nickels*.05)

pennies = int(remainder*100)

print(f"Your amount of ${money} consists of;")
print(f"\t{dollars} dollars")
print(f"\t{quarters} quarters")
print(f"\t{dimes} dimes")
print(f"\t{nickels} nickels")
print(f"\t{pennies} pennies")

