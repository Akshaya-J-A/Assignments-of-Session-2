a=input("Enter a word:")
b=list(reversed(a))
flag =0
for x,y in zip(a,b):
         if x != y:
             flag=1
             break
        
if flag == 1:
    print(" No! “",a,"” is not palindrome")
else:
     print("Yes! “",a,"” is palindrome")
             
        