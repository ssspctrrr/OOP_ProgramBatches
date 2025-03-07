"Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers."

"""num = []

for i in range(1,11):
    num.append(int(input(f"Enter number {i}: ")))

print(sum(num))"""

sum = 0

for i in range(1,11):
    num = int(input(f"Enter number {i}: "))
    sum += num

print(sum)