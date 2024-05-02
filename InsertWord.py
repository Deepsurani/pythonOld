# Original string
string = input(" insert the string ")

# Word to insert
word_insert = input("insert the word ")

# Position to insert the word
position =int(input("insert the pos "))

# Insert the word at the specified position
new_string = string[:position] + " " +word_insert+ " " + string[position:]

# Print the new string
print(new_string)
