"Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers."

even = 0

for i in range(1,11):
    if int(input(f"Enter number {i}: ")) % 2 == 0:
        even += 1

print(f"There are {even} even numbers")