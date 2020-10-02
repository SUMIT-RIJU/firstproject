n=int(input("enter the no:"))
temp=n
rev=0
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
if temp==rev:
    print("this is a palindromeno:")
else:
    print("it is not a palindrome no:")
