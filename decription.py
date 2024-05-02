
msg = input("Enter a message to encrypt: ")
key= int(input("enter the key between 1 to 7 "))
decrypt = ""
for ch in msg:
    asc = (ord(ch) - key)
    each = chr(asc)
    decrypt += each
print("Decrypted message:", decrypt)