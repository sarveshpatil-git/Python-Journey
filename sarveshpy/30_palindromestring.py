a=input("Enter a string:")
b=""

for i in range(len(a)-1,-1,-1):
    b=b+a[i]

if b==a:
    print("It is palindrome")
else:
    print("Not palindrome")    