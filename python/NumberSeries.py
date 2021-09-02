#/////////////////////   ARITHMETIC SERIES    ////////////////////////////


#//////////  sum of numbers series  increment by 1

def  by1(n):
    sum = 0
    for i in range(1,n+1):        
        sum  +=i      
    return sum

# print(by1(9))


#////////////// sum of numbers series increment by 2

def by2(n):
    sum = 1
    a = 2
    for i in range(1,n+1):
        sum += a
        print(sum)
    return sum

# print("the sum of th is ")
# print(by2(5))

#////////// sum of numbers series increment by 4

def by4(n):
    sum = 2
    a = 4
    for i in range(1,n+1):
        sum += a
        print(sum)
    return sum

# print(by4(5))

#////////// sum of numbers series x^1 + x^2 + x^3 ....n
import math
def bypower(x,n):
    sum = 0
    for i in range(1,n+1):
        sum += math.pow(x,i)
        print(sum)
    return sum
# bypower(3,3)


#////////// sum of numbers series 9^2 + 13^2 + 17^3 ....n
import math
def bypower2(x,n):
    sum = 0
    a = 4
    for i in range(1,n+1):
        x += a
        sum += math.pow(x,2)
        print(sum)
    return sum
# bypower2(3,3)

#////////// sum of numbers series 2^x + 4^x + 6^x ....20
import math
def bypowerx(x):
    sum = 0
    a = 2
    for i in range(0,20):
        if(a>20):
            break
        print(a)
        sum += math.pow(a,x)
        a = a +2
        print(sum)
    return sum
# bypowerx(3)

#////////// sum of numbers series 1^3/x + 3^3/x + 5^3/x ....n
import math
def bypowerx3(x,n):
    sum = 0
    a = 1
    for i in range(0,10):
        if(a>n):
            break
        print(a)
        sum += math.pow(a,3)/x
        a = a +2
        print(sum)
    return sum
# bypowerx3(3,5)



#////////////////////////// GEOMETRIC SERIES //////////////////////

# geometric is multiply by constant number
# like  2 + 4 + 8 --- here every numer is multiplying into 2

def geoby2(n):
    sum = 0
    a = 2
    
    for i in range(0,n):
        print(a)
        sum += a
        a = a * 2
    print(sum)
    
# geoby2(4)

#/////// x/2 + x/4 + x/8 ....n

def geobyx(x,n):
    sum = 0
    a = 2
    for i in range(0,n):
        sum += x/a
        print(sum)
        a *=2

# geobyx(20,4)


#//////// 2 - 6 + 8 - 54 .....

def geometric(n):
    a = 2
    sum = 0 
    bool = True
    for i in range(0,n):
        if (bool):
            sum += a
            print(a)
            
            bool = False
        else:
            sum -= a
            print(sum)
            bool = True

        a *=3
# geometric(4)


#///////  (x + 5^2)/1+2 + (x + 25^2)/2+3 + (x + 125^2)/3+4 .....n

def geometrichard(x,n):
    sum = 0
    a = 5
    for i in range(1,n+1):
        sum = sum + (x + math.pow(a,2))/(i+i+1)
        a *= 5
    print(sum)
        
# geometrichard(20,2)



        









