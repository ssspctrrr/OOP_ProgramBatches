"Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number."

num = []

for i in range(1,3):
    num.append(int(input(f"Enter number {i}: ")))

print(num[0] % num[1])