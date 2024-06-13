import string

user_input = input("Enter a string: ")
cleaned_string = user_input.translate(str.maketrans('', '', string.punctuation))
print("String without punctuation:", cleaned_string)