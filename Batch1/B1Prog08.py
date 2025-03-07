"Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers."

odd = 0

for i in range(1,11):
    if int(input(f"Enter number {i}: ")) % 2 == 1:
        odd += 1

print(f"There are {odd} odd numbers")