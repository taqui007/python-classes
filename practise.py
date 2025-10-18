
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

#16
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

# l18=[1,2,3,4,5,6,]
# ev=[]
# od=[]
# for i in l18:
#     if i%2==0:
#         ev.append(i)
#     else:
#         od.append(i)
# print("EVEN:",ev)
# print("ODD:",od)

# ...................................................................

# n=int(input("Enter the number:"))
# l19=[x for x in range(n) if x%2==0 ]
# print(l19)
# s=sum(l19)
# print(s)

#(or)

# n=int(input("Enter the number of elements:"))
# l19=[int(input("Enter the element:")) for _ in range(n)]
# s=sum(x for x in l19 if x%2==0)
# print("Sum of even numbers:",s)

# ..................................................................................

# l20=[int(input(f"Enter the marks for subject{i+1}")) for i in range(5)]
# s=sum(l20)
# a=s/5
# print("Sum of marks:",s)
# print("Avg of marks:",a)

# ..................................................................................

# n=int(input("Enter the number:"))
# l21=[x for x in range(1,n+1)if x%2==0 and x%3!=0]
# print(l21)

# ..................................................................................

# m=[23,45,67]
# n=[12,65,98,23,55]
# l22=[]
# x=min(len(m),len(n))
# for i in range(x):
#     l22.append(m[i])
#     l22.append(n[i])
# l22.extend(m[x:])
# l22.extend(n[x:])
# print(l22)

# ....................................................................................

# a=[11,22,14]
# b=[45,77,88]
# c=[90,99,55,10]
# l23=[[a[i],b[i],c[i]] for i in range(min(len(a),len(b),len(c)))]
# print(l23)

# ......................................................................................

# a=[11,22,14]
# b=[45,77,88]
# c=[90,99,55,10]
# l24=[a[i]+b[i]+c[i] for i in range(min(len(a),len(b),len(c)))]
# print(l24)

# .......................................................................................

# a=[11,22,14]
# b=[45,77,88]
# c=[90,99,55,10]
# l25=[[a[i]%10,b[i]%10,c[i]%10] for i in range(min(len(a),len(b),len(c)))]
# print(l25)

# ........................................................................................

# n=int(input("Enter the number:"))
# s1=set()
# for i in range(n):
#     s1.add(i)
# print(s1)

# ..........................................................................................

# n=int(input("Enter the number of tuples:"))
# s2=set()
# for i in range(n):
#     print(f"Enter the elem for Tuple {i+1}")
#     a=int(input("Enter the elem 1:"))
#     b=int(input("Enter the elem 2:"))
#     c=int(input("Enter the elem 3:"))
#     t=(a,b,c)
#     s2.add(t)
# print(s2)

# ...........................................................................................

# n=int(input("Enter the number:"))
# s3={x for x in range(2,n+1)}
# print(s3)
# for i in s3:
#     sq=i**2
#     print(f"The square of {i} is:",sq)

# ............................................................................................

# n=input("Enter the string:")
# w=n.split()
# s4=set(w)
# for w in s4:
#     print(w)

# .............................................................................................

# n=int(input("Enter the number:"))
# s5={x for x in range(n)}
# if len(s5)==0:
#     print("The set is empty")
# else:
#     print("The set is not empty")

# ..............................................................................................

# e1=set()
# e2=set()
# m=int(input("Enter the number of elem:"))
# n=int(input("Enter the number of elem:"))
# e1={x for x in range(m)}
# e2={x for x in range(n)}
# print(e1)
# print(e2)
# cartesian_product={(x,y) for x in e1 for y in e2}
# print(cartesian_product)

#(or)

# e1=set()
# e2=set()
# m=int(input("Enter the number of elem:"))
# n=int(input("Enter the number of elem:"))
# a1={x for x in range(m)}
# a2={x for x in range(n)}
# print(e1|a1)
# print(e2|a2)
# cartesian_product={(x,y) for x in a1 for y in a2}
# print(cartesian_product)

# ..........................................................................

# m=input("Enter the string1:")
# n=input("Enter the string2:")
# x=set(m.split())
# y=set(n.split())
# print(x)
# print(y)
# u=x&y
# if u:
#     print(u)
# else:
#     print("no common elements")

# ...............................................................................

# s1='wha4ts12ap1p'
# for i in s1:
#     if i.isdigit():
#         print(int(i)**2, end=" ")

# ...............................................................................

# m='abc'
# n='ab'
# cartesian_product=[x+","+y for x in m for y in n]
# print(" ".join(cartesian_product))

# ...............................................................................

# num='1234'
# n=len(num)
# total=0
# for i in range(n):
#     for j in range(i+1,n+1):
#         total+=int(num[i:j])
# print(total)

#process=1+12+123+1234+2+23+234+3+34+4

#(or)

# str = "1234"
# n = len(str)
# l = []

# for i in range(1,n+1):
#     for j in range(i,n+1):
#         l.append(str[i-1:j])

# sum = 0
# for i in l:
#     sum += int(i)

# print(l)
# print(sum)

# .................................................................................

# s5="YOU AND PES"
# print(s5.replace('YOU','I'))

# ..................................................................................

# str1='python'
# str2='code'
# l22=[]
# x=min(len(str1),len(str2))
# for i in range(x):
#     l22.append(str1[i])
#     l22.append(str2[i])
# l22.extend(str1[x:])
# l22.extend(str2[x:])
# print(l22)
# str = ""
# for i in l22:
#     str = str + i
# print(str)

# .............................................................

# s1='whatsapp'
# s2='wat'
# l1 = list(s1)
# l2 = list(s2)
# print(l1)
# print(l2)
# for i in l2:
#     for j in l1:
#         if i == j:
#             l1.remove(j)
# print(l1)
# str=""
# for i in l1:
#     str=str+i
# print(str)

# ...........................................................................

# str="do or die"
# for i in str:
#     if 'd' in str:
#         print(True)
#         break
#     else:
#         print(False)

#(or)

# str="do or die"
# x='d'
# for i in str:
#     if i==x :
#         print(True)
#         break
#     else:
#         print(False)

# ...................................................................

str1='elegant man'
str2='a gentleman'
str1=str1.replace(" ","")
str2=str2.replace(" ","")
if sorted(str1)==sorted(str2):
    print("These are anagrams")
else:
    print("These are not anagrams")