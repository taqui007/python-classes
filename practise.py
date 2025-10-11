
# ......................................................

# n=int(input("Enter the number:"))
# for i in range(1,n+1):
#      print(i)

# .......................................................

# n=int(input("Enter the number:"))
# x=sum(range(1,n+1))
# print("The sum of all the numbers is:",x)

# ........................................................

# n=input("Enter the string:")
# for i in n:
#     print(ord(i))

# .........................................................

# n=int(input("Enter the number:"))
# for i in range(1,n+1,2):
#     print(i)

# ...........................................................

# n=int(input("Enter the number:"))
# for i in range(1,n+1):
#      if i%3==0 and i%5==0:
#         print(i)
#      else:
#         print("The number is not divisible by 3 and 5")
#         break

# ............................................................

# n=int(input("Enter the number:"))
# for i in range(1,n+1):
#     if str(i).endswith('9'):
#         print(i)

# .............................................................

# for i in range(1,11):
#     if i/5!=1: 
#         print(i)

# ...............................................................

# x=input("Enter the first name:")
# y=input("Enter the second name:")
# z=input("Enter the third name:")
# print(x,y,z)

# ...............................................................

# while True:
#      n=input("Enter the number or type stop:")
#      if n=='stop':
#           print("The prog has been stopped.")
#           break
#      elif int(n)%2==0:
#       print("The number is even")
#      else:
#          print("The number is odd")

# ...............................................................

# import random
# print(random.uniform(1,1000))


# 11
# 12

# .................................................................

# n=int(input("Enter the number:"))
# d=[i for i in range(1,n) if n%i==0]
# if sum(d)==n:
#     print("The number is perfect")
# else:
#     print("The number is not perfect")

# ....................................................................

#14

# .....................................................................

#15

# .....................................................................

# for i in range(100,1000):
#     s=str(i)
#     if s==s[::-1]:
#         print("All three digit palindrone numbers are",i)

# .....................................................................

# n=int(input("Enter the number:"))
# f=[i for i in range(1,n) if n%i==0]
# print(f"The factors of {n} are: ",f)

# .......................................................................

#18

# ..........................................................................

# n=int(input("Enter the number:"))
# print(f"The hexadecimal of {n} is:",hex(n))
# print(f"The octal of {n} is:",oct(n))

# .........................................................................

# n=int(input("Enter the number:"))
# print(f"The reverse of {n} is:",n[::-1])

# ...........................................................................

# n=int(input("Enter the number:"))
# for i in range(10):
#     print(n, "X", i+1, "=", n*(i+1))

# ............................................................................

# n=int(input("Enter the side1:"))
# a=int(input("Enter the side2:"))
# b=int(input("Enter the side3:"))
# c=int(input("Enter the side4:"))
# d=int(input("Enter the diagonal1:"))
# e=int(input("Enter the diagonal2:"))
# if n==a==b==c==d==e:
#     print("The quadrilateral is a square")
# elif n==b and a==c and d==e:
#     print("The quadrilateral is a rectangle")
# elif n==b and a==c:
#     print("The quadrilateral is a rhombus")
# elif n==b and a==c:
#     print("The quadrilateral is a parallelogram")
# else:
#     print("The given figure is just a quadrilateral")

# ............................................................................

#23

# ............................................................................

#24

# ............................................................................

#identity matrix pattern:
# n=4
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print(1, end=' ')
#         else:
#             print(0, end=' ')
#     print()

# ............................................................................

#number matrix pattern 
# n=4
# num=1
# for i in range(n):
#     for j in range(n):
#         print(num,end=" ")
#         num+=1
#     print()

# .............................................................................

# a=int(input("side1:"))
# b=int(input("side2:"))
# c=int(input("side3:"))
# if (a+b>c) and (b+c>a) and (c+a>b):
#     if a==b==c:
#         print("Equilateral traiangle")
#     elif a==b or b==c or c==a:
#         print("Ispsceles triangle")
#     else:
#         print("Scalene triangle")
# else:
#     print("Cannot form a triangle")

# ...............................................................................

#27
# z="May i have a large container of coffee?"

# ...............................................................................

# import math
# r=float(input("Enter the radius:"))
# d=2 * r
# a=math.pi * r**2
# c=2 * math.pi * r**2
# print(f"d:{d:.2f}")
# print(f"a:{a:.2f}")
# print(f"c:{c:.2f}")

# ...............................................................................

# s=int(input("Decimal number:"))
# print(f"Binary of {s} is:",bin(s))

# ................................................................................

# n=int(input("Enter the number:"))
# for i in range(1,n+1):
#     if n%2==0:
#         print("The given number is EVEN")
#         break
#     else:
#         print("The given number is ODD")
#         break

# ................................................................................

# l1=[1,2,3]
# for i in l1:
#     print(i)

# ...............................................................................

# l2=[]
# n=int(input("Enter the number:"))
# for i in range(1,n+1):
#  l2.append(i)
# print(l2)

# ................................................................................

# l3=[1,2,3]
# li=[x**2 for x in l3]
# print(li)

# ................................................................................

# import math
# l4=[1,4,9]
# li=[math.sqrt(x) for x in l4]
# print(li)

# ................................................................................

#leftmost msg
# l5=[1,2,3,4]
# y=next(x for x in l5 if x%2==0)
# print(f"The leftmost even number is:{y}")

# ..................................................................................

# n=int(input("Enter the number:"))
# l6=[1,2,3,4]
# l6=[x+n for x in l6]
# print(l6)

# ....................................................................................

# l7=[1,2,3,4]
# li=[abs(l7[i+1]-l7[i])for i in range(len(l7)-1)]
# print(li)

# .....................................................................................

# l8=["zenitsu",7,True,3.0]
# int=[x for x in l8 if isinstance(x,int) and not isinstance(x,bool)]
# str=[x for x in l8 if isinstance(x,str)]
# bool=[x for x in l8 if isinstance(x,bool)]
# floats=[x for x in l8 if isinstance(x,float)]
# print("Integers:",int)
# print("String:",str)
# print("Boolean:",bool)
# print("Floats,:",floats)

# ....................................................................................

# l9=[x for x  in range(2,20,2) if x %4!=0]
# print(l9) 

#(or)

# l9=[x for x  in range(2,20)if x%2==0 and x%4!=0]
# print(l9)

# ....................................................................................

# l10=[1,2,2,3,3,3]
# li=list(dict.fromkeys(l10))
# print("New list without duplicates:",li)

#(or)

# l10=[1,2,2,3,3,3]
# li=[]
# for i in l10:
#     if i not in li:
#         li.append(i)
# print("original list:",l10)
# print("New list without duplicates:",li)

# ...................................................................................

# l11=[9,3,5,2,7]
# l11.sort()
# print("The sorted list is:",l11)

# ....................................................................................

# n=int(input("Enter the number:"))
# l12=[1,2,3,4,5]
# y=next((x for x in l12 if x>n),None)
# if y is not None:
#     print(f"The leftmost number greater than {n} is:",y)
# else:
#     print(f"No number greater than {n} is:",y)

#(or)

# n=int(input("Enter the number:"))
# l12=[1,2,3,4,5]
# k=0
# for i in l12:
#     if i>n:
#         print(f"The leftmost number greater than {n} is:",i)
#         k=1
#         break
# if k!=1 :
#     print(f"The number greater than {n} is not present in our list")

# .................................................................................

# n=int(input("Enter the number:"))
# l13=[i for i in range(1,n+1) if i!=n//2]
# print(l13)

# .................................................................................

# n=int(input("Enter the number:"))
# l14=[i for i in range(n,0,-1)]
# li=[i for i in range(2,n+1)]
# l14.extend(li)
# print(l14)

# ..................................................................................

# n=int(input("Enter the number:"))
# l15=[ [i for i in range(1,n+1)],
#       [i**2 for i in range(1,n+1)],
#       [i**3 for i in range(1,n+1)]
# ]
# print(l15)

# ....................................................................................

# n=int(input("Enter the number:"))
# seq=[i*i+1 for i in range(1,n+1)]
# total=sum(seq)
# print(seq)
# for i in range(1,n+1):
#     seq=i*i+1 
#     t=sum(seq)
#     if i 

# Input number of terms
# n = int(input("Enter the number of terms: "))

# Initialize sum
# total = 0

# Display sequence
# print("The sequence is: ", end="")

# for i in range(1, n + 1):
#     term = i * (i + 1)
#     total += term
    # To print the sequence properly with '+'
    # if i != n:
    #     print(f"{i} * {i + 1} + ", end="")
    # else:
    #     print(f"{i} * {i + 1}", end="")

# Display result
# print(f" = {total}")

# ...........................................................................

# l17=[1,2,3,4,6,9,12]
# li=len([x for x in l17 if x%3==0])
# print(li)

# ............................................................................

l18=[1,2,3,4,5,6,]
ev=[]
od=[]
for i in l18:
    if i%2==0:
        ev.append(i)
    else:
        od.append(i)
print("EVEN:",ev)
print("ODD:",od)
        
l18=[1,2,3,4,5,6,]
ev=[]
od=[]
for i in l18:
    if i%2==0:
        ev.append(i)
    else:
        od.append(i)
print("EVEN:",ev)
print("ODD:",od)
