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
# reverseWithPreserve("i am string")


# 6) REVERSE A WORD IN A GIVEN STRING 
# eg :  hello world -> olleh dlrow

def reverseWord(str):
    str = str.split(" ")
    list = []
    
    for i in range(0,len(str)):
        list.append(str[i][::-1])
    str1 = " "
    print(str1.join(list))

# reverseWord("hello world")

# 7) Program to print first non repeated character from String

def nonRepeatChar(str):
    
    for i in range(0,len(str)):
        count = False

        for j in range(0,len(str)):
            if(str[i] == str[j]) & (i !=j):
                count  = True
                break
        if(count == False):
            return str[i]

    return "no"
            
# print(nonRepeatChar("aaabbccddffpg"))


def nonrepeating(str):

    counts = {}
    order = []

    for i in str:
        if i in counts:
            counts[i] +=1
            
        else:
            counts[i] = 1
            order.append(i)
    for j in order:
        if counts[j] == 1:
          return j
    return None
    
# print(nonrepeating("helooooopphel"))


# 7) b) Program to print first non repeated character from String using WHILE LOOP


def demo(str):

    while str !="":
        len1 = len(str)
        char = str[0]
        str = str.replace(char,"")
        len2 = len(str)

        if len2 == len1-1:
            print(" the first unique char is ",char)
            break
        else:
            print("no unique char")
# demo("pooven")



# 8) Check whether the given string is only contains numbers

import re
from typing import Counter

def findonlydigits(str):
    str1 = str.split(" ")
    str2 = "".join(str1)  #this is process to delete all empty spaces in the string
    print(str2)
    newstr = re.findall("[0-9]",str2)
    if len(str2) == len(newstr):
        print("this string contains only digits")
    else:
        print("this is not digits")

# findonlydigits("0009")


# 9) reverse String in Java using Iteration and Recursion?

def reversestr(str):
    newstr = ""
    for i in str:
        newstr = i + str
    print("reverse string using iteration :",end=" ")
    print(newstr)
# reversestr("hello world exexcuse me")

def reversestr1(str):
    if(len(str)==0):
        return str
    else:
        return reversestr1(str[1:]) + str[0]

# print(reversestr1("hello world"))

# 10) find duplicate characters 

def dupChar(str):

    counts = {}
    for i in str:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
            
    
    for i in counts:
        if counts[i] > 1:
            print(i ,end=":")
            print(counts[i])

# dupChar("poovendhan")

# 11) count vowels and consonants in a given string
import re
def vowelcounter(str):
    vowel = 0
    consonsnts = 0
    str = str.replace(" ","")
    print(str)

    count = re.findall("[aeiouAEIOU]",str)
    vowel = len(count)
    consonsnts = len(str) - vowel

    print("vowels :",vowel)
    print("consonants :",consonsnts)
    

vowelcounter("nithees kumar")
