
sentence = input("Enter the sentence: ")
updated_sentence = ""
for i in range(len(sentence)-1,-1, -1):
    updated_sentence+=sentence[i]
if sentence==updated_sentence:
    print("this is a "+updated_sentence+" is palindrome")
else:
    print("this is "+updated_sentence+" is not a palindrome")