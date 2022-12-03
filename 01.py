with open('input/01_input.txt') as file:
    lines = [line.strip() for line in file]

i = 1
calories = {}
calories[i] = 0
for food in lines:
    if food == '':
        i += 1
        calories[i] = 0
    else:
        calories[i] += int(food)

print(calories[max(calories, key=calories.get)])
top = sorted(calories, key=calories.get, reverse=True)[:3]
sum = calories[top[0]] + calories[top[1]] + calories[top[2]]
print(sum)
