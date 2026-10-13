
f = open("myfile.txt", "r")

content = f.read()

vowels = "aeiouAEIOU"
count = 0

for ch in content:
    if ch in vowels:
        count += 1

f.close()

print("Total number of vowels:", count)
