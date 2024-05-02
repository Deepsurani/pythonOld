A=input("Enter Your Name:-")
B=input("Enter Product Name:-")
C=input("Enter Product Price:-")
D=input("Enter The Qty:-")
E=int(C)*int(D)
print("_________________________________________________________")
print("total="+str(E))
f=0
if E>=1500:
    f=(E * 15)/100
    print("discount=" +str(f)+"(15%)")
elif  E>=1000:
       f=(E * 10)/100
       print("discount=" +str(f)+"(10%)")
elif E>=500:
    f=(E * 5)/100
    print("discount=" +str(f)+"(5%)")
elif E<=500:
    f=(E * 2)/100
    print("discount=" +str(f)+"(2%)")
T=int(E)-int(f)
print("NET Amount:-"+str(T))
print("thank You,"+A+"\tVisit Again")