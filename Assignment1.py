a = [45, 56, 98, 3, 67, 9, 90]
b = a[0]#initializing with first element of a
print("Array Elements:",a)
for x in a:
    if x>b:
        b=x
print("Largest in the Array :",b)