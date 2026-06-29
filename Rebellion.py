a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    c=arr.count(0)
    d=len(arr)-c
    count=0
    coun=c
    for i in range(len(arr)):
        if arr[i]==1:
            l=i+1
            r=len(arr)-i
            e=min(d,r)+count
            if e>coun:
                coun=e
        else:
            count+=1
    print(len(arr)-coun)
