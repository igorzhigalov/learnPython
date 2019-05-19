s='У лукоморья 123 дуб зеленый 456'
print(s.find('я'))
print(s.count('у'))
if s.isalpha():
    print(s)
else:
    print(s.upper())
length_string=len(s)
if length_string>4:
    print(s.lower())
'O'+s[1:]
