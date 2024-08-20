def fibonacci_sequence(num1,num2):
    n = int(input("How Many Times You Want To Run : "))
    for i in range(n):
        temp = num1 + num2
        num1 = num2
        num2 = temp
        print(temp,end=" ")
num1 = int(input("Enter The Number1 : "))
num2 = int(input("Enter The Number2 : "))

fibonacci_sequence(num1,num2)


'''
OUTPUT:-

Enter The Number1 : 1
Enter The Number2 : 2
How Many Times You Want To Run : 5
3 5 8 13 21 
'''