print("===BILL CALCULATOR===")
print()
print()


myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = float(input("What percentage tip would you like to give? 15, 10, 25, 5, 0: "))
print()

myTip = tip/100
myTip = myTip * myBill
billTip = myTip + myBill 
answer = billTip / numberOfPeople
answer = round(answer, 2)
print("You all owe", "\033[36m", answer, "\033[0m")