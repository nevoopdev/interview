#  PATTERNS PROGRAM

# 1) INCREASING TRIANGLE PATTERN 
#   *
#   * *
#   * * *
#   * * * *

def itp():
    n= int(input("enter nth term : "))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("* ",end="")
        print()
# itp()

# 2) DECCREASING TRIANGLE PATTERN 
# * * * *
# * * *
# * *
# *

def dtp():
    n= int(input("enter nth term : "))
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print("* ",end="")
        print()

# dtp()


# 3) RIGHT SIDED TRIANGLE PATTERN 
#     *
#    **
#   ***
#  ****

def rst1():
    n= int(input("enter nth term : "))
    a = n
    for i in range(1,n+1):
        for j in range(a,0,-1):
           
            print(end=" ")
        for k in range(1,i+1):
            print("* ",end="")
        print()
        a -=1
# rst1()


# 4) RIGHT SIDED TRIANGLE  PATTERN 2
# * * * * 
#   * * * 
#     * * 
#       * 

def rst2():
    n= int(input("enter nth term : "))
    a = 1
    for i in range(n,0,-1):
        for j in range(a,0,-1):
            print("  ",end="")
        for k in range(i,0,-1):
            print("* ",end="")
        print()
        a +=1

# rst2()



# 5) HILL PYRAMID OR FULL PYRAMID

def pryamid():
    n= int(input("enter nth term : "))
    a = n + n
    b = 1
    for i in range(1,n+1):
        for j in range(a,0,-1):
            print(end=" ")
        for k in range(1,b+1):
            print("*",end=" ")
        print()
        a -=2
        b +=2
# pryamid()


# 6) reverse pyramid  not full pyramid
def pryamid1():
    n= int(input("enter nth term : "))

    for  i in range(1,n+1):
        for j in range(n,i-1,-1):
            print(end=" ")
        for k in range(1,i):
            print("*",end=" ")
        print()
          
   
    for i in range(1,n+1):
        
        for j in range(2,i+1):
            print(end=" ")
        for k in range(n,i-1,-1):
            print("*",end=" ")
        print()
    

# pryamid1()



# 6) REVERSE FULL PYRAMID

def reverse():
    n= int(input("enter nth term : "))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(end=" ")
        for k in range(n,i,-1):
            print("*",end=" ")
        for l in range(n,i-1,-1):
            print("*",end=" ")
        print()
# reverse()
        

        


