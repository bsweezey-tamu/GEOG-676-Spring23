# Part 1 - Multiply all list items together
part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
result1 = 1

for i in part1:
    result1 = result1 * i

print('The result of the first question is:', result1)

# Part 2 - Add all list items together
part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]
result2 = 0

for i in part2:
    result2 = result2 + i

print('The result of the second question is:', result2)

# Part 3 - Add together ONLY even numbers in list
part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21] 
result3 = 0

for i in part3:
    if i % 2 == 0:              # Using the Modulo operator to divide by 2 and look at remainder
        result3 = result3 + i

print('The result of the third question is:', result3)