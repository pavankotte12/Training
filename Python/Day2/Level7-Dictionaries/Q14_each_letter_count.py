# Take a from user and print dictionary showing how many times each letter is repeated  
word = input("Enter a word:")
#To store each character
freq={}
# Looping through string if character is already in dictionary
for c in word:
    if c in freq:
    # If present then increase its count to 1
        freq[c]+=1
    else:
        #Set frequeny to 1
        freq[c] = 1

print(f"Displaying repeated letters in a word {freq}")

