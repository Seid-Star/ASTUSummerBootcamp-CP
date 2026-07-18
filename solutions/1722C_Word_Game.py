from collections import Counter
a=int(input())
for x in range(a):
    d=0
    e=0
    f=0
    b=int(input())
    arr=list(map(str,input().split()))
    brr=list(map(str,input().split()))
    crr=list(map(str,input().split()))
    c=Counter(arr)
    g=Counter(brr)
    h=Counter(crr)
    for i in arr:
        l=g[i]+h[i]
        if l==2:
            d+=0
        elif l==1:
            d+=1
        else:
            d+=3
    for j in brr:
        l=c[j]+h[j]
        if l==2:
            e+=0
        elif l==1:
            e+=1
        else:
            e+=3
    for k in crr:
        l=c[k]+g[k]
        if l==2:
            f+=0
        elif l==1:
            f+=1
        else:
            f+=3
    print(d,e,f)