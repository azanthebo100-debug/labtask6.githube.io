data = {'a': 1, 'b': 2, 'c': 3}
reverse = {}
for key in data:
    value = data[key]
    reverse[value] = key
print(reverse)