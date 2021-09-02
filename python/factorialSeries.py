#/////////////   FACTORIAL SERIES ////

# //// 1! + 2!+ 3!+......N

def factby1(n):
    sum = 0
    for i in range(1,n+1):
        fact = 1
        print("i is .....",i)
        for j in range(1,i+1):
            fact =fact * j
            print("j is :",j)
            print("fact of ",j,"is ",fact)
        sum += fact
    print(sum)
factby1(5) 