# CTI-110 
# P2HW2 - Tip Tax Total 
# Anthony Jackson
# 2/20/18



BillTotal =float(input("Enter Bill Total $    "))

tip = 0.18 * BillTotal

salesTax = .07 * BillTotal

total = BillTotal + tip + salesTax

print ("Bill Total $" + format(BillTotal, ",.2f"))

print ("tip $" + format(tip, ",.2f"))

print ("salesTax $" + format(salesTax, ",.2f"))

print ("total $" + format(total, ",.2f"))







