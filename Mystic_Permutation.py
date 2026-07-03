a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    brr=[]
    for i in range(1,len(arr)+1):
        brr.append(i)
    for j in range(len(arr)-1):
        if arr[j]==brr[j]:
            brr[j],brr[j+1]=brr[j+1],brr[j]
    if len(arr)==1:
        print(-1)
    else:
        if brr[-1]==arr[-1]:
            brr[-1],brr[-2]=brr[-2],brr[-1]
        print(*brr)



