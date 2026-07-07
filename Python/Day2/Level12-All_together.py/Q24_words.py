# Display number of words, longest word and every word capitalized from a sentence
sentence = input("Enter the sentence: ")

# Split the sentence into words
words = sentence.split()

# Number of words
word_count = len(words)

# Longest word
longest_word = max(words,key=len)

# Capitalize every word
capitalized_sentence = sentence.title()

# Output
print(f"Number of words: {word_count}")
print(f"Longest word: {longest_word}")
#print(f"Capitalized sentence: {capitalized_sentence}")
result = ""
for word in words:
    result += word.capitalize() + " "
print(result.strip())