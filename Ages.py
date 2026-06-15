A = int(input("Enter a age Ajay "))
V = int(input("Enter a age Vijay "))
R = int(input("Enter a age Ravi "))
if(R<V and R<A):
    youngest= R
elif(V<R and V<A):
    youngest= V
else:
    youngest= A
print("Youngest is age",youngest )
  
print("------------2nd Method-------------")

a = int(input("Enter a age Ammi "))
b = int(input("Enter a age Bunny "))
c = int(input("Enter a age Cat "))
if(a>b):
  if(a>c):
    print ("a is greater")
  else:
     print("c is greater")
else:
   if(b>c):
     print("b is graeter")
   else:
      print("c is graeter")


