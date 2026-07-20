a=int(input())
for x in range(a):
    b,c=map(int,input().split())
    arr=list(map(int,input().split()))
    crr=[]
    err=set()
    for i in range(len(arr)):
        if arr[i] not in err:
            err.add(arr[i])
            crr.append(i+1)
            if len(crr)==b:
                break
    drr=[]
    d=b-len(crr)
    for i in range(d):
        drr.append(-1)
    frr=drr+[0]*len(crr)
    for k in range(len(crr)):
        frr[b-1-k]=crr[k]
    print(*frr)
