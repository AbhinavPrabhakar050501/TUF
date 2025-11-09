#PATTERN 1
# for i in range(4):
#     for j in range(4):
#         print("*",end="")
#     print()   

# for i in range(1,5): 
#         print("*"*i,end="")
#     print()   

#PATTERN 2
# for i in range(5): 
#     for j in range(i): 
#         print("*",end="")
#     print()   

#PATTERN 3
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()    

#PATTERN 4
# for i in range(1,6):
#     for j in range(i):
#         print(i,end="")
#     print()    

# PATTERN 5
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()    

#PATTERN 6
# for i in range(6,1,-1):
#     for j in range(1,i):
#         print(j,end="")
#     print()    

#PATTERN 9 = 7 + 8
# PATTERN 7
# for i in range(5):
#     for j in range(5-i-1):
#         print(" ",end="")
#     for j in range(2*i+1):
#         print("*",end="")
#     for j in range(5-i-1):
#         print(" " ,end="")
#     print()    

# #PATTERN 8
# for i in range(5,0,-1):
#     for j in range(5-i):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     for j in range(5-i):
#         print(" " ,end="")
#     print()    


#PATTERN 10
# n = 5
# for i in range(1,2*n):
#     stars = i
#     if i > n:
#         stars = 2*n - i
#     for j in range(stars):
#         print("*",end="")
#     print()    

#PATTERN 11
n = 5

for i in range(1,n+1):
    num = 0
    for j in range(i):
        if i%2 != 0 and j%2 == 0:
            num +=1
        print(num,end="")
        # num-=1
    print()
