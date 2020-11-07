t=int(input())
for i in range(1,t+1):
    x=int(input())
    y=int(input())
    if(x==y):
        print((x+x)**2)
    elif(x>y and y+y>=x):
        print((y+y)**2)
    elif(x>y and y+y<x):
        print((x)**2)
    elif(y>x and x+x>=y):
        print((x+x)**2)
    elif(y>x and x+x<y):
        print((y)**2)
