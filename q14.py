print("Enter lines of text. Enter an empty line to finish.")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
print("You entered:")
for line in lines:
    print(line)