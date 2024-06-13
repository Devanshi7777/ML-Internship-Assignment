user_input = input("Enter a string: ")
frequency = {}
for char in user_input:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print("Character frequency:", frequency)