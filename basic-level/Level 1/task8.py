#8️. Calculate simple interest

#Formula: (P * R * T) / 100

p = int(input("enter Principle: "))

r = int(input("enter Rate: "))

t = int(input("enter Time(in years) : "))

interest = p*r*t/100

print("Simple interest is", interest)

amt = p + interest

print("Total amount is", amt)
