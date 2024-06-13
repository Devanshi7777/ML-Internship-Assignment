numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
element = int(input("Enter the element to count: "))
print(f"{element} occurs {numbers.count(element)} times in the list.")