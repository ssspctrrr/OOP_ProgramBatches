"Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers."

num = []

for i in range(1,11):
    num.append(int(input(f"Enter number {i}: ")))

print(num[0] - sum(num[1:]))

