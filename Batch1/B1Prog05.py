"Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point"

num = []

for i in range(1,3):
    num.append(float(input(f"Enter number {i}: ")))

print(num[0] / num[1])

#0:44