# n=int(input("Enter the number:"))
# def solo(n):
#     s='abcd'
#     for i in range (n):
#         print(s[i:]) 
# solo(n)

# or

# for i in range(4):
#     for j in range(97+i,101):
#         print(chr(j),end="")
#     print()

# (or)

s=input("Enter the characters:")
n=len(s)
def solo():
    for i in range (n):
        print(s[i:])
solo()

# ................................................................................................

# n=int(input("Enter the number:"))
# def solo():
#  for i in range(n):
#   print(str(i+1)*(i+1))
# solo()

#or

# n=int(input("Enter the number:"))
# def solo():
#  for i in range(n):
#   for j in range(i+1):
#    print(str(j+1)*(j+1))
# print()
# solo()

# .....................................................................................

l=[12,34,8.9,3+6j,"Level",[1,2,3],{1:111,2:222}]
def create_list():
    types=set()
    for i in l:
        types.add(type(i))
    l1=[[],[],[]]

    for i in range(len(types)):
        l1.append([])
    for i in l1:
        if type(i)==int:
            l1[0].append(i)
        elif type(i)==float:
            l1[1].append(i)
        elif type(i)==complex:
            l1[2].append(i)
    return l1
print("List created as follows")
print(create_list())

#(or)

# l=[12,34,8.9,3+6j,"Level",[1,2,3],{1:111,2:222}]
# int=[x for x in l if isinstance(x,int) and not isinstance(x,bool)]
# float=[x for x in l if isinstance(x,float)]
# string=[x for x in l if isinstance(x,str)]
# bool=[x for x in l if isinstance(x,bool)]
# complex=[x for x in l if isinstance(x,complex)]
# dict=[x for x in l if isinstance(x,dict)]
# print(int)
# print(float)
# print(string)
# print(bool)

# ...............................................................................

# n=input("Enter the sentence:")
# def rev():
#     words=n.split()
#     for i in words:
#         print(i[::-1])
# rev()

# ...................................................................................

# n=int(input("Enter the limit:"))
# def generate_fibonacci(n):
#     a=0
#     b=1
#     print(a,b, end=" ")
#     for i in range(2,n):
#         c=a+b
#         print(c, end=" ")
#         # a=b
#         # b=c
#         a,b = b,c
# generate_fibonacci(n)

# ...................................................................................

# n=input("Enter the sentence:")
# def create_dictionary():
#     words_count={}
#     words=n.split()
#     unique_words=set(words)
#     for i in words:
#         words_count[i]=words.count(i)
#     for k,v in words_count.items():
#         print(k,"--",v)
#     print(words_count)
# create_dictionary()

# .....................................................................................

# n=20
# sieve=set(range(2,n+1))
# while(sieve):
#     smallest=min(sieve)
#     print(smallest)
#     sieve=sieve-set(range(smallest,n+1,smallest))

# ....................................................................................