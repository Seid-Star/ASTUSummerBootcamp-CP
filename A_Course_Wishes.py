a=int(input())
for x in range(a):
    b,c=map(int,input().split())
    arr=list(map(int,input().split()))
    brr=list(map(int,input().split()))
    crr=[]
    for i in range(len(brr)):
        crr.append((brr[i],i+1))
    crr.sort(reverse=True)
    drr=[]
    for j,k in crr:
        while j<c+1:
            drr.append(k)
            j+=1
    print(len(drr))
    print(*drr)
