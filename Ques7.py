# Q7. Write a python script to determine whether a string contains a specific substring.?
s1=input("Enter a String:")
s2=input("Enter a Substring:")
if s2 in s1:
    print(s2,"String Found in",s1)
else:
    print(s2,"Not Found in",s1)

