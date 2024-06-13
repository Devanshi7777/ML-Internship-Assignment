main_string = input("Enter the main string: ")
substring = input("Enter the substring: ")
if substring in main_string:
    print(f"'{substring}' is present in '{main_string}'.")
else:
    print(f"'{substring}' is not present in '{main_string}'.")