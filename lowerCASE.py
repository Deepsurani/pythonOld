msg = input("Enter a message: ")
uppercase = ""

for ch in msg:
    if 'A' <= ch <= 'Z':
        asc = ord(ch) +32
        each = chr(asc)
        uppercase += each
    else:
        uppercase += ch  

print(" message:", uppercase)