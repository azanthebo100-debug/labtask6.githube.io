marks = { 'azan': 85,
    'zaheer': 95,
    'haniya': 95,
    'aimal': 78 }
highest = max(marks.values())
for name in marks:
        if marks[name] == highest:
         print(name, ":", marks[name])