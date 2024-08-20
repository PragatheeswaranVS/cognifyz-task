import random
random_number = random.randint(1,100)
while True:
    number = int(input("Enter Any Number From 1-100 : "))
    diff = number - random_number
    if diff == 0:
        print(f"You Guessed Number {number} Correctly")
        break
    elif diff > 0:
        print(" Too High")
    else:
        print(" Too Low")
        
'''
OUTPUT:-

Enter Any Number From 1-100 : 55
 Too Low
Enter Any Number From 1-100 : 80
 Too High
Enter Any Number From 1-100 : 76
You Guessed Number 76 Correctly

'''