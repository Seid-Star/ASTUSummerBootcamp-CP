a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    c=arr.count(min(arr))
    if c==b:
        print(0)
    else:
        print(len(arr)-c)