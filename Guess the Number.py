#### Guess the Number
import random
print("Nishanth M Y, USN: 1AY24AI078, SEC: O")
num = int(input("Enter the number between 1 to 9: "))
while num < 1 or num > 9:
    num = int(input("Invalid input! Please enter a number between 1 to 9: "))
print(num, "is the number entered by user")
comp_num = random.randint(1, 9)
print(comp_num, "is the number randomly taken by computer")
if num == comp_num:
    print("User guess is Absolutely Correct!!!!!!!!!!")
else:
    print("Oh NO! User guess is Incorrect!!!!!!!!!!")
