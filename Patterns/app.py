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
# n = 5

# for i in range(1,n+1):
#     num = 0
#     if i%2 == 0:
#         num = 0
#     else: 
#         num = 1
#     for j in range(i):
#         print(num,end="")
#         num  = 1 - num 
#     print()

#PATTERN 12
# n = 5
# num = 0
# space = 2*(n-1)
# for i in range(0,n):
#     # num += 1
#     for j in range(1,i+1):
#         # num += 1
#         print(j,end="")
#     for j in range(space):
#         # num += 1
#         # print(j)
#         print(" ",end="")
#     for j in range(i,0,-1):
#         # num += 1
#         print(j,end="")
#     space -= 2    
#     print()  



#PATTERN 13
# n = 5
# num = 0

# for i in range(1,n+1):
#     # num += 1
#     for j in range(i):
#         num += 1
#         print(num,end="")
#     print()    


# PATTERN 14

# for i in range(65,71):
    # for j in range(65,i+1):
    #     print(chr(j), end="")
    # print()    



# PATTERN 15
# for i in range(70,65,-1):
#     for j in range(65,i):
#         print(chr(j), end="")
#     print()    

# PATTERN 16
# for i in range(65,71):
#     for j in range(65,i+1):
#         print(chr(i), end="")
#     print()   

#PATTERN 17
# n=5

# for i in range(n):
#     ch = 65
#     bp = (2*i+1) / 2
#     for j in range(n-i-1):
#         print(" ",end="")

#     for j in range(1,2*i+2):
#         print(chr(ch),end="") 
#         if j <= bp:
#             ch+=1
#         else:
#             ch-=1    
#     for j in range(n-i-1):
#         print(" " ,end="")
#     print()   


#PATTERN 18
# n = 5
# ch = 70
# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print(chr(ch-j),end="")   
#     print()

#PATTERN 19
# n = 5
# for i in range(1,n):
#     for j in range(n-i+1):
#         print("*",end="")
#     for j in range(2*i-4):
#         print(" ",end="")
#     for j in range(n-i+1):
#         print("*" ,end="")
#     print() 

# for i in range(5,1,-1):
#     for j in range(n-i+1):
#         print("*",end="")
#     for j in range(2*i-4):
#         print(" ",end="")
#     for j in range(n-i+1):
#         print("*" ,end="")
#     print() 

#PATTERN 20
# n = 5

# for i in range(5,1,-1):
#     for j in range(n-i+1):
#         print("*",end="")
#     for j in range(2*i-4):
#         print(" ",end="")
#     for j in range(n-i+1):
#         print("*" ,end="")
#     print() 

# for i in range(1,n):
#     for j in range(n-i+1):
#         print("*",end="")
#     for j in range(2*i-4):
#         print(" ",end="")
#     for j in range(n-i+1):
#         print("*" ,end="")
#     print() 

# PATTERN 20
n = 4
for i in range(n):
    for j in range(n):
        print('*',end="")
    print()   




