a=int(input())
for x in range(a):
    b,c=map(int,input().split())
    d=input().strip()
    arr=[]
    for i in range(b,0,-1):
        arr.append(i)
    brr=[]
    l=0
    r=len(arr)-1
    i=0
    while i<len(d):
        if d[i]=='0':
            brr.append(arr[l])
            l+=1
        else:
            brr.append(arr[r])
            r-=1
        i+=1
    e='1'*c
    if e in d:
        print("NO")
    else:
        print("YES")
        print(*brr)
