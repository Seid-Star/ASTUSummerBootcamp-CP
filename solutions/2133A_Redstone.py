a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    if len(set(arr))<b:
        print("YES")
    else:
        print("NO")