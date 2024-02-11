a = input("Enter the string: ")
a = a.lower()
b = 0
char = ""

for x in a:
    c = a.count(x)
    if c >= b:
        b = c
        char = x

print(char, "is repeated the most")
