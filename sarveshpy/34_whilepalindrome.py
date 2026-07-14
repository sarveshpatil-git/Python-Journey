ori=int(input("Enter a number:"))
temp=ori
rev=0
while ori>0:
    rev=rev*10+ori%10
    ori=ori//10

if temp==rev:
    print("It is a palindrome number.")
else:
    print("Not a palindrome number.")
