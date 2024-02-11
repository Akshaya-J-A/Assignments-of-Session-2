a=[45, 73, 105, 7, 54, 80]
b=[]

for x in a:
    d1=x//100
    d2=x%10
    d3=(x//10) % 10
    sum=d1+d2+d3
    b.append(sum)
    
print(b)


