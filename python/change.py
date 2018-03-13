c=float(input("Please enter your amount"))
c = c*100
print(c//25, "Quarters")
c = c%25
print(c//10, "Dimes")
c = c%10
print(c//5, "Nickels")
c = c%5
print(c//1, "Pennies")
