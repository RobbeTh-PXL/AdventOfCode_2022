import numpy as np
file_path = "Day5\data.txt"

buffer_line = []
buffer_char = []

with open(file_path) as file:
    for lines in file:
        for character in lines:
            if (character != '[' or character != ']') and character.isupper():
                buffer_char.append(character)
            if character == "0" or character == "1" or character == "2" or character == "3" or character == "4" or character == "5" or character == "6" or character == "7" or character == "8" or character == "9":
                buffer_line.append(character)

print(buffer_char)
print(buffer_line)
