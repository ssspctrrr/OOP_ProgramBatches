"Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers."

num = []

for i in range(1,3):
    num.append(int(input(f"Enter number {i}: ")))

for j in range(num[0] + 1, num[1]):
    print(j)