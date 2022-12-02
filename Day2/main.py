file_path = "Day2\data.txt"

# Open and read file, close when done
with open(file_path, 'r') as f:
    lines = f.readlines()
f.close()

# Replace newline chars
list_clean = []

for item in lines:
    list_clean.append(item.replace("\n", ""))

# Calculate score
x = 0

for item in list_clean:
    if item == "A X":
        x += 4
    elif item == "A Y":
        x += 8
    elif item == "A Z":
        x += 3

    elif item == "B X":
        x += 1
    elif item == "B Y":
        x += 5
    elif item == "B Z":
        x += 9

    elif item == "C X":
        x += 7
    elif item == "C Y":
        x += 2
    elif item == "C Z":
        x += 6
    else:
        print("Unknown")
        break

print(x)

# Calculate score
x = 0

for item in list_clean:
    if item == "A X":
        x += 3
    elif item == "A Y":
        x += 4
    elif item == "A Z":
        x += 8

    elif item == "B X":
        x += 1
    elif item == "B Y":
        x += 5
    elif item == "B Z":
        x += 9

    elif item == "C X":
        x += 2
    elif item == "C Y":
        x += 6
    elif item == "C Z":
        x += 7
    else:
        print("Unknown")
        break

print(x)