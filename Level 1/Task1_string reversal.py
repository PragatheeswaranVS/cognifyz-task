def reverse(str):
    str = str[::-1]
    return str
string = input("\nEnter a string : ")
res = reverse(string)
print(f"The reverse of the string is {res}\n")