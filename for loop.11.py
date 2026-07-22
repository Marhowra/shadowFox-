import random

roll_6 = 0
roll_1 = 0
two_6_row = 0
previous = 0

for i in range(20):
    dice = random.randint(1, 6)
    print("Roll", i + 1, ":", dice)

    if dice == 6:
        roll_6 += 1

    if dice == 1:
        roll_1 += 1

    if previous == 6 and dice == 6:
        two_6_row += 1

    previous = dice

print("Number of times 6 appeared:", roll_6)
print("Number of times 1 appeared:", roll_1)
print("Two consecutive 6s:", two_6_row)