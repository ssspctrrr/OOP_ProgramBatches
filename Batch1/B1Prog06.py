"Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number."

num = []

for i in range(1,3):
    num.append(int(input(f"Enter Number {i}: ")))

print(num[0] ** num[1])