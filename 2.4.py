TAX = 0.07
cost1 = float(input("please enter a price :"))
cost2 = float(input("please enter a price2 :"))
cost3 = float(input("please enter a price3 :"))
cost4 = float(input("please enter a price4 :"))
cost5 = float(input("please enter a price5 :"))

total = cost1 + cost2 + cost3 + cost4 + cost5
tax = total * TAX
print(f"You total is {tax+total:.2f}, with tax of {tax:.2f} included")
