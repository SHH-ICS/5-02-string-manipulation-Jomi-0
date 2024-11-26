# Create a program that will accept a word from a user and return the length of that word. 
# Make this program in a loop with option to exit when the use types in quit.
word=(input("Type a word: "))
if word.lower() == 'quit':
        print("Goodbye!")
if word.isalpha :
    print("You have",len(word)," letters")
    
else:
    print("Input must be a word")

