with open("nginx_logs.txt", "r", encoding="utf-8") as text:
    cont_slice = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in text)
    for i in cont_slice:
        print(i)
