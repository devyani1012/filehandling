
f = open("myfile.txt", "r")

lines = f.readlines()

f.close()

print("All lines:", lines)
print("Total number of lines:", len(lines))

print("Second line:", lines[1])
