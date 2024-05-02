a = input("Enter your maths marks:")
while (100<int(a)):
      a=input("Enter valid marks")

b = input("Enter your sci marks:")
while (100<int(b)):
      b=input("Enter valid marks")

c = input("Enter your guj marks:")
while (100<int(c)):
      c=input("Enter valid marks")

d = input("Enter your eng marks:")
while (100<int(d)):
      d=input("Enter valid marks")
e = input("Enter your hindi marks:")
while (100<int(e)):
      e=input("Enter valid marks")
print("_____________________________________________________________________")

Ans = int(a)+int(b)+int(c)+int(d)+int(e)

print("\n Total is  " + str(Ans))
g1=0
g2=0
g3=0
g4=0
g5=0
if int(a) < 40 or int(b) < 40 or int(c) < 40 or int(d) < 40 or int(e) < 40:
      if int(a)<40:
            g1 = 40 - int(a)
      if int(b) < 40:
            g2 = 40 - int(a)
      if int(c) <40:
            g3 = 40 - int(c)
      if int(d) <40:
            g4 = 40 - int(d)
      if int(e) <40:
            g5 = 40 -int(e)
      gtotal = g1 +g2 +g3+g4+g5
      if gtotal <= 8:
            print("you Are pass with Paasing marks")
      else:
            print("You Are fail")
else:

      p = int(Ans)/5

      print("\n per:"+str(p) + " % ")
      if p>=70:
          print("Grade A")
      elif p >= 60:
          print("Grade B")
      elif p>=50:
          print("Grade C")
      elif p>=40:
          print("Grade D")