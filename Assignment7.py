def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

vowels=['a','e','i','o','u']
a=input("Enter the String:")
a=a.lower()
b=[]
for x in a:
    if x not in vowels:
        b.append(x)
print(listToString(b))