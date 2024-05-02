main_string = input("Enter The String: ")
FindW = input("Enter The Word To Find: ")
count=0
Count_index=0
for i in range(len(main_string)):
    j = main_string.find(FindW,Count_index)
    if(j!=-1):
	    start_index = j+1
count+=1
print("Total Find are: ", count)
