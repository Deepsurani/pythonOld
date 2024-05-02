str = input("Enter the sentence: ")
delete_char = input("Please Enter Delete Char: ")

new_str = ""
for i in range(len(str)):
    if str[i] != delete_char:
        new_str += str[i]

print("The modified string is: ", new_str)
