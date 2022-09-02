a=input()
b=a.lower()
c=b.count('a')
d=b.count('o')
if c>0 or d>0:
    print(f"Буква 'a' встречается {c} раз")
    print(f"Буква 'o' встречается {d} раз")
else:
    print(f"В введенном предложении нет букв 'o' и 'a'")