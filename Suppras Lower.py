str = input("Enter the sentence: ")
print("The original string is: " + str)

count = 0
res = ""

for i in str:
    if 'a' <= i <= 'z': 
        res += i
        count += 1

print("The Lower characters in string are: " + res)
print('Number of Lower characters: ', count)
