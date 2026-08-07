a=int(input())
for x in range(a):
    b,c=map(int,input().split())
    d,e=map(int,input().split())
    f=b-c
    g=d-e
    if f*g<0:
        print("NO")
    else:
        print("YES")