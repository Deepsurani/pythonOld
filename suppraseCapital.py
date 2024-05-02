str = input("Enter the sentence: ")
print("The original string is: " + str)

count = 0
res = ""

for i in str:
    if 'A' <= i <= 'Z': 
        res += i
        count += 1

print("The uppercase characters in string are: " + res)
print('Number of uppercase characters: ', count)
