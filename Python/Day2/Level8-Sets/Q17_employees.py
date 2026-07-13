# Displaying unique words from a sentence
sentence = input("Enter a sentence: ").lower()

#Splitting the sentence
unique_words = set(sentence.split())

#Length of unique words
no_of_unique_words = len(unique_words)

print(f"Unique words in the sentence are {no_of_unique_words}")

