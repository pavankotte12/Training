# Ask the user to enter a sentence and
sentence = input("Enter a sentence: ")

try:
    words = sentence.split()

    # Check if the sentence has at least one word
    first_word = words[0]

    # Print the number of words
    print("Number of words:", len(words))

    # Print the longest word
    longest_word = max(words, key=len)
    print("Longest word:", longest_word)

    # Capitalize every word
    capitalized_sentence = " ".join(word.capitalize() for word in words)
    print("Capitalized sentence:", capitalized_sentence)

except IndexError:
    print("Error: You entered an empty sentence.")

finally:
    print("Done")