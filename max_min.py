A=int(input ("Enter First Value:"))
B=int(input ("Enter Second Value:"))
C=int(input ("Enter 3rd value "))

if (A> B and A > C):
  print(str(A)+" Max Value Than "+str(B)+" And "+str(C))

elif (B> A and B > C):
    print(str(B)+"Max value Than "+str(C)+" And "+str(A))

elif (C > B and C > A):
    print(str(C)+"max value than"+str(B)+ " And " +str(A))

elif (A==B and B==C):
    print("Three Value Are Same😁")