a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    brr=(sorted(arr))
    if arr==brr:
        print(b)
    else:
        print(1)