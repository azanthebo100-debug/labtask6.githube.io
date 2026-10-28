words = ['apple','ant','banana','ball','cat']
group = {}
for word in words:
    first = word[0]
    if first in group:
        group[first].append(word)
    else:
        group[first] = [word]
print(group)