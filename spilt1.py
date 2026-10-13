
f = open("myfile.txt", "r")

content = f.read()

f.close()

words = content.split()

print("Total number of words:", len(words))

unique_words = set(words)

print("Unique words:", unique_words)
