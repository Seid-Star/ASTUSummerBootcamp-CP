a=int(input())
for x in range(a):
    b=int(input())
    brr=[]
    for i in range(b):
        arr=list(map(int,input().split()))
        for i in arr:
            if i not in brr:
                brr.append(i)
    c=(2*b)
    d=(c*(c+1))//2
    e=d-sum(brr)
    crr=[e]
    drr=crr+brr
    print(*drr)
