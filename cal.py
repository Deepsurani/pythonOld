A=int(input("Enter the First Value:-"))
B=int(input("Enter the Second Value:-"))

print("Your options\n1)for sum\n2)for minus\n3)for multi\n4)fpr div\n")

C=int(input("enter Your choice😉"))

if int(C)==1:
    print("Ans="+str(int(A)+int(B)))
elif int(C)==2:
    print("Ans="+str(int(A)-int(B)))

elif int(C)==3:
    print("Ans"+str(int(A)*int(B)))

elif int(C)==4:
    print("Ans"+str(int(A)/int(B)))