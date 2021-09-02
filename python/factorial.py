def factorial(num):
    if num < 1:
        return num
    count = 1

    for i in range(1,num+1):
        count = count * i
    print("the factorial of given number is :" ,end="")
    return count
   
print(factorial(5))