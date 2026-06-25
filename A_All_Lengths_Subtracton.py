a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    l=0
    r=len(arr)-1
    count=1
    found=True
    while l<r:
        if arr[l]==count:
            l+=1
        elif arr[r]==count:
            r-=1
        else:
            found=False
            break
        count+=1
    if found:
        print("YES")
    else:
        print("NO")
