char_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# for i in char_list:
#     for j in range(1,5,2):
#         for k in range(j):
#             print(i,end="")
#         print()

for i in range(5):
    for j in range(65,91):
        print(chr(j),end="")
    print()