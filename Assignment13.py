a=[34, "word", 4.5, "code", 89, 9.0]
b={}
for x in a:
    item_type = type(x).__name__
    if item_type in b:
        b[item_type].append(x)
    else:
        b[item_type] = [x]
print(b)
        
        