units = int(input("please Enter the number of units used:"))
if units<50:
    amount = 2.60 * units
    tax = 25
elif units<=100:
    amount = 3.25 * units
    tax = 35
else:
    amount = 5.26 * units
    tax = 45
total = amount+tax
print("Electricity Bill is:",total)
