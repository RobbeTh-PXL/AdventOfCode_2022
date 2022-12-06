file_path = "Day3\data.txt"

# Find alphabetic place
def prio(character):
    if character.islower():
        return ord(character) - 96
    elif character.isupper():
        return ord(character) - 38
    else:
        print("Unknown Character")

# Part1
sum = 0
with open(file_path) as file:
	for line in file:
		line = line.strip()
		c1 = {char for char in line[: len(line) // 2]}
		c2 = {char for char in line[len(line) // 2 :]}
		sum += prio(c1.intersection(c2).pop())

print(sum)

# Part2
sum = 0
with open(file_path) as file:
	buffer = []
	for line in file:
		buffer.append({char for char in line.strip()})
		if len(buffer) == 3:
			sum += prio(buffer[0].intersection(buffer[1], buffer[2]).pop())
			buffer = []

print(sum)


"""
References:
https://www.reddit.com/user/BrainPuppet/
https://www.w3schools.com/python/ref_string_strip.asp               -> Cleanup line
https://www.w3schools.com/python/ref_set_intersection.asp           -> Find similar char
https://www.programiz.com/python-programming/methods/list/pop       -> Remove item from list at index
"""