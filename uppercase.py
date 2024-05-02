msg = input("Enter a message: ")
uppercase = ""

for ch in msg:
    if 'a' <= ch <= 'z':
        asc = ord(ch) -32
        each = chr(asc)
        uppercase += each
    else:
        uppercase += ch  

print("Uppercase message:", uppercase)
