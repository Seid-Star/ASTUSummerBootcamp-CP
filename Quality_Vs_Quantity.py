a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    brr=sorted(arr)
    l=0
    r=len(arr)-1
    R=brr[r]
    B=brr[l]+brr[l+1]
    r=r-1
    l=l+2
    while l<r:
        R+=brr[r]
        B+=brr[l]
        l+=1
        r-=1
    if R>B:
        print("YES")
    else:
        print("NO")
        
