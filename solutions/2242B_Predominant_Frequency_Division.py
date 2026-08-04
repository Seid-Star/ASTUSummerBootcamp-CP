a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    brr=[0]*(b+1)
    crr=[0]*(b+1)
    for i in range(1,b+1):
        brr[i]=brr[i-1]
        crr[i]=crr[i-1]
        if arr[i-1]==1:
            brr[i]+=1
            crr[i]+=1
        elif arr[i-1]==2:
            brr[i]-=1
            crr[i]+=1
        else:
            brr[i]-=1
            crr[i]-=1
    drr=[-10**18]*(b+1)
    drr[b-1]=crr[b-1]
    for i in range(b-2,0,-1):
        drr[i]=max(drr[i+1],crr[i])
    Seid=False
    for l in range(1,b-1):
        if brr[l]>=0 and drr[l+1]>=crr[l]:
            Seid=True
            break
    if Seid:
        print("YES")
    else:
        print("NO")
 