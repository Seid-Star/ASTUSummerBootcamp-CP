a,b=map(int,input().split())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
crr=[0]*(len(arr)+1)
l=1
for i in arr:
    crr[l]=crr[l-1]+i
    l+=1
k=1
for j in brr:
    while j>crr[k]:
        k+=1
    print(k,j-crr[k-1])
 