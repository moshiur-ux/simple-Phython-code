t = int(input(""))
type(t)
for x in range(1,t+1):
     a=int(input(""))
     b=int(input(""))
     c=int(input(""))
     if(a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b):
         print("case %i:  YES"%x)
     else:
         print("case %i: NO"%x)
