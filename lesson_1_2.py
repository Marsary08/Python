numbers = []
all_sum = 0
new_all_sum = 0
num = 0
new_sum = 0
for cube_number in range(1, 1000, 2):
    cube_number **= 3
    numbers.append(cube_number)

print(numbers)

for number in numbers:
    save_num = number
    while number != 0:
        num = save_num % 10
        new_sum += num
        num = save_num // 10
        save_num = num
        if save_num == 0:
            break
    if new_sum % 7 == 0:
        all_sum += number
        new_sum = 0
    else:
        new_sum = 0
print(all_sum)

for number in numbers:
    number += 17
    save_num = number
    while number != 0:
        num = save_num % 10
        new_sum += num
        num = save_num // 10
        save_num = num
        if save_num == 0:
            break
    if new_sum % 7 == 0:
        new_all_sum += number
        new_sum = 0
    else:
        new_sum = 0
print(new_all_sum)
