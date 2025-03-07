"Prog03: Create a program that ask user to input 2 numbers. Print the sum of the two numbers."

num = []

for i in range(1,3):
    num.append(int(input(f"Enter nummber {i}: ")))

print(num[0] + num[1])

#0:59

sum = 0

for i in range(1,3):
    num = int(input(f"Enter number {i}: "))
    sum += num

print(sum)