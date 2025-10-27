# u=int(input("Enter initial velocity:"))

# a=int(input("acceleration:"))

# t=int(input("Enter time:"))

# v=u+a*t

# s=u+(1/2)*a*t*t

# print("The initial velocity is", v)

# print("The distance travelled is", s)

# # ..............................................................................

# n=input("Enter the name:")
# a=int(input("Enter the age:"))
# print(f"Name:{n}, Type:{type(n)},ID: {id(n)}")
# print(f"Age:{a}, Type:{type(a)},ID: {id(a)}")

# n=int(input("Enter the number:"))
# print(f"Type of n:{type(n)}")
# for i in range(1,11):
#  print(n, "X", i, "=", n*i)

# from math import pi
# r=int(input("Enter the radius:"))
# d=2*r
# c=2*pi*r
# a=pi*r**2
# print(f"radius:{d}")
# print(f"circumference:{c}")
# print(f"area:{a}")
# print(f"ID of radius is {id(r)}")

# n=int(input("Enter the number:"))
# n=str(n)
# n=n[::-1]
# n=int(n)
# print(n)

# n=int(input("Enter the decimal number:"))
# print(bin(n))
# print(type(n))
# print(type(bin(n)))

# n=int(input("Enter the quantity:"))
# cost=n*100
# if cost>2000:
#     print(f"cost is:{cost-(cost*0.15)}")
# elif cost>1000:
#     print(f"cost is:{cost-(cost*0.1)}")
# else:
#     print(f"cost is:{cost}")

n=int(input("Enter the quantity:"))
if n>1:
    for i in range(2,n):
        if n%i!=0:
            print("it is prime")
            break
        else:
            print("it is not prime")
            break
else:
    print("invalid number")








# # n=int(input("Enter the year:"))
# # if n%400==0:
# #     print(f"{n} is a leap year")
# # elif n%4==0 and n%100!=0:
# #     print(f"{n} is a leap year")
# # else:
# #     print(f"{n} is not a leap year")

# # for i in range(3,10,2):
# #     for j in range(1,i,2):
# #         print(j,end=' ')
# #     print()

# # a=int(input("Enter the first no:"))
# # b=int(input("Enter the second no:"))
# # i=0
# # while i<5:
# #     print("Menu:")
# #     print("1.add")
# #     print("2.sub")
# #     print("3.mul")
# #     print("4.div")
# #     i=int(input("Enter the choice between 1 to 4:"))
# #     if i==1:
# #         print(a+b)
# #         break
# #     elif i==2:
# #         print(a-b)
# #         break
# #     elif i==3:
# #         print(a*b)
# #         break
# #     elif i==4:
# #         print(a/b)
# #         break
# #     else:
# #         print("invalid choice")
#         break

# n=int(input("Enter the n:"))
# x=int(input("Enter the x:"))
# for i in range(n):
#   sum=0
#   sum= lambda x:(x**n)
#   print(sum(x))
#   break

# x= int(input("Enter the value of x:"))
# n= int(input("Enter value of n (for x **n):"))
# s = 0
# for a in range(n+1):
#  s+= x**a
#  print("Sum of first", n, "terms:", s)

# n = int(input("enter a num :"))
# m = int(input("enter a base :"))
# sum = 0
# for i in range(n+1):
#     if(i == n):
#         print(f"{m}^{i}", end=" ")
#     else:
#         print(f"{m}^{i}", end=" + ")
#     sum += m**i

# print("=", sum)

# n = int(input("enter a num :"))
# sum = 0
# for i in range(n+1):
#     if(i == n):
#         print(f"{2}^{i}", end=" ")
#     else:
#         print(f"{2}^{i}", end=" + ")
#     sum += 2**i

# print("=", sum)

# n = int(input("enter a num :"))
# print(bin(n))

# Program to print the given pattern of alphabets

# ch = 65  
# for i in range(1, 6):  
#     for j in range(1, 2 * i):  
#         print(chr(ch), end=" ")
#         ch += 1
#     print()  

# total = 0
# while True:
#     num = input("Enter a positive integer (or 'q' to quit): ")
#     if num.lower() == 'q':
#         break  
#     if not num.isdigit():  
#         print("Invalid input. Enter a positive integer.")
#         continue
#     num = int(num)
#     if num > 100:
#         print(f"{num} is greater than 100, ignored.")
#         continue
#     total += num
# print(f"Sum of valid numbers: {total}")


# def f2():
#  print("in f2")
# def f1():
#  print("in f1")
#  global f2
# def ff2():
#  print("in ff2")
# f1()
# f2()
# ff2()

# a = 10
# print(id(a))
# a= a+10
# print(id(a))

