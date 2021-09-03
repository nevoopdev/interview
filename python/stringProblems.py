# 1) REVERSE A STRING 
def reverse(str):
    print(str[::-1])

# reverse("pooven")

# 2) PALINDROME CHECKING

def palindrome(str):

    reversedstr = str[::-1]
    if(reversedstr == str):
        print(str, " is palindrome")
    else:
        print(str, " is not palindrome")

# palindrome("madam")

# 3) Print duplicate characters from String?

def duplicateStr(str):
    
    for i in range(0,len(str)):
        count = 0
        char = str[i]
        for j in range(i,len(str)):
            if(char == str[j]):
                count += 1
        if(count == 2):
            print(str[i])

# duplicateStr("poovvennnnnnsss")

# 4)  a)CHECK IF TWO STRING ARE ANAGRAM OR NOT

def anagram(str1,str2):
    if(len(str1) != len(str2)):
        print("this is not anagram ")
        return
    bool = True
    for i in range(0,len(str1)-1):
        check = str2.find(str1[i])
        if(check == -1):
            bool = False
    if(bool):
        print("this is anagram")
    else:
        print("this is not an anagram")

# anagram("listen","silentkk")


#   b) using sort method

def anagramSort(str1,str2):
    if(sorted(str1) == sorted(str2)):
        print("this is anagram")
    else:
        print("this is not anagram")
# anagramSort("listen","silentjj")


# 5) Revere String With Preserve spaces 

def reverseWithPreserve(str):
    l = len(str)
    list = ["0"] * l
    for i in range(0,len(str)-1):
        if(str[i]== " "):
            list[i] = " "
    j =  l -1
    
    for i in range(0,len(str)):
        if(str[i] != " "):
            if(list[j] == " "):
                j -= 1
            list[j] = str[i]
            j -=1
    str1 = ""
    print(str1.join(list))
   

        
    
reverseWithPreserve("poovven is some")





    

     
    
 

