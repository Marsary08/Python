arr = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
sentence = []

for symbol in arr:
    if symbol.replace("+", "").replace("-", "").isdigit():
        if symbol.isdigit():
            sentence.append(f"'{int(symbol):02}'")
        else:
            sentence.append(f"'{symbol[0]}{int(symbol[1:]):02}'")
    else:
        sentence.append(symbol)
print(arr)
print(" ".join(sentence).capitalize())
