#Easy-level
#program to check even or odd
# def even_or_odd(n):
#     if n%2==0:
#         return "Even"
#     else:
#         return "Odd"
# print(even_or_odd(int(input("Enter a value:- "))))

#largest number
# n1=int(input("Enter first number:- "))
# n2=int(input("Enter second number:- "))
# if n1>n2:
#     print(n1,"is greater")
# else:
#     print(n2,"is greater")

#+ve,-ve,zero
# n=int(input("Enter a number:- "))
# if n>0:
#     print("Positive")
# elif n<0:
#     print("Negative")
# else:
#     print("Zero")

#eligibility 
# age=int(input("Enter your age:- "))
# if age>18:
#     print("Eligible to vote")
# else:
#     print("Not Eligible to vote")

#prime or not
# n=int(input("Enter a number:- "))
# if n%2==1:
#     print("Prime number")
# else:
#     print("Not a prime number")

#number revese
# n=int(input("Enter a number:- "))
# rev=0
# while n:
 
#  ld=n%10
#  rev=rev*10+ld
#  n=n//10
# print(rev)

#check palindrome
# word=input("Enter a word:-")
# if word==word[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

#second largest in a list
# n=eval(input("Enter a list: "))
# n.remove(max(n))
# second=max(n)
# print("Second Largest number in list is",second)

n=eval(input("Enter a list:- "))

for i in range(len(n)):
    count=0
    for j in range(len(n)):
    
        if n[i]==n[j]:
            count+=1
    print(n[i],"appeares ",count,"times")

