msg = input("Enter a message: ")
Toggle = ""
for ch in msg:
    if 'a' <= ch <= 'z':
        asc = ord(ch) -32
        each = chr(asc)
        Toggle += each
    elif 'A' <=ch <='Z':
        asc =ord(ch)+32
        each = chr(asc)
        Toggle+=each

print("Uppercase message:", Toggle)
