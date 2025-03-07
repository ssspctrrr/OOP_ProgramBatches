"Prog01: Create a program that ask user to input 2 numbers. Print the bigger number."

nums = []

for i in range(1,3):
    nums.append(int(input(f"Enter number {i}: ")))

print(nums)

if nums[0] > nums[1]:
    print(f"{nums[0]} is bigger.")
elif nums[0] < nums[1]:
    print(f"{nums[1]} is bigger.")
else:
    print("The numbers are equal.")