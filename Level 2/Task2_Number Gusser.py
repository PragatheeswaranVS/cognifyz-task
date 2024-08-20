import random
start = int(input("Enter The Starting Range : "))
end = int(input("Enter The Ending Range : "))
random_number = random.randint(start,end)
while True:
    number = int(input(f"Enter Any Number From ({start}-{end}) : "))
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

Enter The Ending Range : 100
Enter Any Number From (1-100) : 77
 Too High
Enter Any Number From (1-100) : 50
 Too Low
Enter Any Number From (1-100) : 67
 Too High
Enter Any Number From (1-100) : 61
You Guessed Number 61 Correctly
'''