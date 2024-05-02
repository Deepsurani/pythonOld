str = input("Enter the sentence: ")
Newchar = input("Please Enter New Char: ")
pos = int(input("Enter Position: "))

NewStr = ""
for i in range(len(str)):
    if i == pos:
        NewStr += Newchar
    NewStr += str[i]

print("The modified string is: ", NewStr)
