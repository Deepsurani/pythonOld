name = input("Enter name: ")
r = input("Enter character to count: ")
count=0
positions = ''

for char in range(len (name)):
    if name[char] == r:
        count+=1
        positions += str(char) + ' '

print("The name after count is: ",count)
print("position of character is",positions)
