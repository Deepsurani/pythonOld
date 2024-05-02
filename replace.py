
sentence = input("Enter the sentence: ")
replace = input("Choose the character you want to replace: ")
replace_char = input("Enter the replacement character: ")
updated_sentence = ""

for letter in sentence:
    if letter == replace:
        updated_sentence += replace_char
    else:
        updated_sentence += letter

# Print the updated sentence
print("Updated sentence:", updated_sentence)
