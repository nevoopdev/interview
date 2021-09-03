#/////////////   FACTORIAL SERIES ////

#  1)1! + 2!+ 3!+......N
# ! exlamation means factorial of that number


def factby1(n):
    sum = 0
    for i in range(1,n+1):
        fact = 1
        print("i is .....",i)
        for j in range(1,i+1):
            fact =fact * j
        sum += fact
    print(sum)
# factby1(5) 


#  2)9! + 13! + 17! + ....n
# ! exlamation means factorial of that number

def factby4(n):
    sum = 0
    a =9
    for i in range(1,n+1):
        fact = 1
        for j in range(1,a+1):
            fact *=j
        sum +=fact
        a += 4
    print(sum)
# factby4(2)

#  3)x^1/1! + x^2/2! + .....n

import math

def factcomplex():
    x = int(input())
    n = int(input())
    sum = 0
    for i in range(1,n+1):
        fact = 1
        for j in range(1,i+1):
            fact *=j
        sum += math.pow(x,i)/fact
        print(sum)
# factcomplex()


#  4)1+x/2! + 11+x/4! + 21+x/8!.......


def factcomplex1():
    x = int(input("enter a number x:"))
    n = int(input("enter number of term n:"))
    a = 1
    b = 2
    sum = 0

    for i in range(1,n+1):
        fact = 1
        for j in range(1,b+1):
            fact *= j
        sum = (a + x)/fact
        a +=10
        b *= 2
    print(sum)
# factcomplex1() 


# 5) (1+x)!/2! + (2+x)!/4! + (3+x)!/8! + ....n

def fact(n):
    if(n == 0 | n == 1):
        return 1
    return n * fact(n-1)

def factcomplex3():
    x = int(input("enter a number x:"))
    n = int(input("enter number of term n:"))
    a = 2
    sum = 0

    for i in range(1,n+1):

        fact1 = fact(i+x)
        fact2 = fact(a)
        sum += fact1/fact2
        a *=2
    print(sum)
factcomplex3()












