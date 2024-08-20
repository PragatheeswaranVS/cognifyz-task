import string

def word_occurrence(filename):
    try:
        # Read the entire file content
        with open(filename, "r", encoding='utf-8') as file:
            content = file.read()
            
        # Process the content: normalize, remove punctuation, and split into words
        translator = str.maketrans("", "", string.punctuation)
        words = [word.strip().lower().translate(translator) for word in content.split()]
        
        # Count the occurrences of each word using a dictionary
        word_count = {}
        for word in words:
            if word:
                word_count[word] = word_count.get(word, 0) + 1
        
        # Sort and print the results
        sorted_word_count = dict(sorted(word_count.items()))
        print("\nThe Words and the Number of Words Presented in the Text file are:\n")
        for word, count in sorted_word_count.items():
            print(f"{word} : {count}")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied for file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    word_occurrence(filename)


'''
OUTPUT:-

Enter the filename:  
c:\\Users\\praga\\Desktop\\cognifyz tasks\\Level 2\\Task5_file word count.txt   
The Words and the Number of Words Presented in the Text file are:

beetroot : 1
brinjal : 1
cabbage : 1
calliflower : 1
capsicum : 1
carrot : 2
onion : 2
potato : 2
raddish : 1
sweetpotato : 1
tomato : 3
'''