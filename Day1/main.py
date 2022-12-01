file_path = "Day1\data.txt"

# Open and read file, close when done
with open(file_path, 'r') as f:
    lines = f.readlines()
f.close()

# Replace newline chars
list_clean = []

for item in lines:
    list_clean.append(item.replace("\n", ""))

# Check list format
if list_clean[-1]:
    list_clean.append("")

# Find max sum
x = []
y = 0

for item in list_clean:
    if not item:
        x.append(y)
        y = 0
    else:
        y += int(item)

print("The elf carrying the most is elf %d, carrying %d" % (x.index(max(x)), max(x)))

# Find and sum top 3 elves
x.sort(reverse=True)
print("The top 3 elves are carrying a total of %d calories" % sum(x[0:3]))