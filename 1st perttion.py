k=0
Name=input("Enter The Name: ")

len=len(Name)
for i in range(0,len,1):
    for j in range(0,i+1,1):
        if k<len:
            print(Name[k],end="\t")
            k+=1;
        else:
              print("*",end="\t")
    if (k>len-1):
        break
    print("")
