a= [45, 78, 4, 34, 67, 3, 93, 101, 77]
b=[]
for x in a:
    if x%2 != 0:
        b.append(x)
print("List Elements :",a)
print("List of Odd Numbers :",b)