# Original string
string = input("Enter The String")
words = string.split(' ')
reversed_words = [''.join(reversed(word)) for word in words]
reversed_String = ' '.join(reversed_words)
print(reversed_String)
