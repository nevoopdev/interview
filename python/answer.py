# 1)  PRINT PRIME NUMBERS 1 TO 100 
def primenumber(n):
    for i in  range(2,n+1):
        if(i>1):
          for j in range(2,i):
              if(i % j == 0):
                  break
          else:
           print(i)
# primenumber(100)

# 2) FIBONACCI SERIES

def fibonacci(n):
    
    a = 0
    b = 1
    c = 1
    print(a)
    for i in range(1,n+1):
        print(c)
        c= a+b
        a = b
        b = c
# fibonacci(20)


# 3) PALINDROME 

def palindrome(str):
    reversestr = str[::-1]
    if(str == reversestr):
        print(str," is palindrome")
    else:
      print(str," is not palindrome") 

# palindrome("madamm")


# 4) factorial using recursion

def fact(n):
    if(n==0):
        return 1
    else:
        return n * fact(n-1)

# print(fact(9))

# 5) SWAP PROGRAM WITHOUT THIRD VARIABLE

def swap(a,b):
    print("before swap")
    print(a,b)
    a = a + b
    b = a - b
    a = a - b
    print("after swap")
    print(a,b)
# swap(10,20)

    



    
 
    
