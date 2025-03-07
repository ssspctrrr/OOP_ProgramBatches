'Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.'

num = []

for i in range(1,3):
    num.append(int(input(f"Enter number {i}: ")))

if num[0] == num[1]:
    print("Equal")
else:
    print("Not Equal")

#1:16