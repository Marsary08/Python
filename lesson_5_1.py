def generate_odd_num(num):
    for num in range(1, num + 1, 2):
        yield num


for i in generate_odd_num(int(input("Enter number: "))):
    print(i)
