a=int(input()) 
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    brr=set()
    r=len(arr)-1
    while r>=0:
        if arr[r] in brr:
            break
        brr.add(arr[r])
        r-=1
    print(r+1)
