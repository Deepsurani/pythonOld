word=input("enter the sentence:-")
count=0
vowels=set("aeiouAEIOU")  # set of all vowels 
for letter in word:
    if letter in vowels:
        count += 1
print("vowel is",count)