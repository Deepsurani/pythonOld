
sentence = input("Enter the sentence: ")
updated_sentence = ""
for i in range(len(sentence)-1,-1, -1):
    updated_sentence+=sentence[i]
print("Updated sentence:", updated_sentence)