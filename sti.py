
sentence = input("Enter a sentence: ")

words = sentence.split()

print("List of words:", words)

longest_word = max(words, key=len)

print("Longest word:", longest_word)
