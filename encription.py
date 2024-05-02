
msg = input("Enter a message to encrypt: ")
key= int(input("enter the key between 1 to 7 "))
encrypt = ""
for ch in msg:
    asc = (ord(ch) + key)
    each = chr(asc)
    encrypt += each
print("Encrypted message:", encrypt)