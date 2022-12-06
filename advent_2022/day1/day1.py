"""
ADVENT OF CODE - DAY 1 
"""
with open('C:/Users/User/Desktop/Advent-of-code/2022/Day1/day1.txt', 'r') as file:
    data = [i for i in file.read().strip().split("\n")]

"""
Part 1: Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""
# Store the Calories of each Elf
calories_per_elf = []
count = 0

for i in data:
    # If the line is blank, it means it has reached the end of the current elf's food.
    if i == '':
        calories_per_elf.append(count)
        count = 0 # Resetting the count for the next Elf

    else:
        count += int(i)
    
answer1 = max(calories_per_elf)
print("Answer1:",answer1)

"""
Part 2: Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""
#reverse if is true, sorts in descending order.
#[:3] -> items from the beginning through n-1

#sort and take the top three Elves carrying the most Calories.
a=(sorted(calories_per_elf, reverse=True)[:3]) 
answer2=sum(a)
print("Answer2:",answer2)
