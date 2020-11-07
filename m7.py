e=[int(i) for i in input().split()]
#n=int(input())
#type(n)
while(e!=0):
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    m=a*b
    if(m%2==0):
        print(int(m/2))
    else:
        print(int(m/2+1))
        e=e-1
