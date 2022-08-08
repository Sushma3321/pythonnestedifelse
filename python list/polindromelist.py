# Write a code that checks whether a list is a palindrome or not. And print “Haan! palindrome hai” if its a pallindrome and “nahi! palindrome nahi hai” if its not a palindrome.

# For the time being you can use the list given below for writing the code.

name=[ 'n', 'i', 't', 'i', 'n' ]
i=1
na=[]
while i<=len(name):
     na.append(name[-i])
     i=i+1
print(na)
if name==na:
     print("polindrome")
else:
     print("not polindrome")
     
         
       