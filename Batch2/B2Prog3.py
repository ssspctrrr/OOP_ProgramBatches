"Prog03: Create a program that ask user to input 2 numbers. Print the difference of the two numbers."

num = []

for i in range(1,3):
    num.append(int(input(f"Enter number {i}: ")))

print(num[0] - num[1])