def palindromecheck(word,length):
    reverse = word[::-1]
    if word == reverse:
        return ("It Is Palindrome")
    else:
        return ("It Is Not a Palindrome")
        
word = input("Enter a Word : ")
length = len(word)
res = palindromecheck(word,length)
print(res)


'''
OUTPUT:-

Enter a Word : malayalam
It Is Palindrome

Enter a Word : cognifyz
It Is Not a Palindrome
'''