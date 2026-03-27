# 1️0. Check if a number is divisible by 5 and 11

num = float(input("Enter the your number: "))

if num % 5 == 0 and num % 11 == 0:
    print(f"{num} is divisble by 5 and 11")

else:
    print(f"{num} is NOT divisble by 5 and 11")
