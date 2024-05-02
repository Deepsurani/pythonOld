V=int(input("Enter Value👌:-"))

print("Your Choice\n1)$ TO ₹\n2)₹ TO $\n3)Foot TO CM\n4)CM TO Foot\n5)KM TO Meter\n6)KG TO POUND\n7)POUND TO KG\n8)℉ To ℃\n9)℃ TO ℉")

C=int(input("Enter Your Choice"))

if int(C)==1:
    print("Ans="+str(int(V)*82))

elif int(C)==2:
    print("Ans="+str(int(V)/82))

elif int(C)==3:
    print("Ans="+str(int(V)*38.48))

elif int(C)==4:
    print("Ans="+str(int(V)/38.48))

elif int(C)==5:
    print("Ans="+str(int(V)*1000))

elif int(C)==6:
    print("Ans"+str(int(V)*2.205))

elif int(C)==7:
    print("Ans="+str(int(V)/2.205))

elif int(C)==8:
    print("Ans="+str((int(V)-32)*5/9))

elif int(C)==9:
    print("Ans="+str((int(V)*9/5)+32))