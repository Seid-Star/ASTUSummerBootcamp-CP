a=int(input())
for x in range (a):
    b,c=map(int,input().split())
    if b%c==0:
        print("YES")
    else:
        print("NO")