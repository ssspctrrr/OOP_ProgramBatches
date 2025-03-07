"Prog01: Create a program that ask user to input 2 numbers. Print the smaller number."

num = []

for i in range(1,3):
    num.append(int(input(f"Enter number {i}: ")))

if num[0] == num[1]:
    print("The numbers are equal.")
elif num[0] < num[1]:
    print(f"{num[0]} is smaller.")
else:
    print(f"{num[1]} is smaller.")