a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    brr=list(map(int,input().split()))
    crr=[]
    for i in range(len(arr)):
        if i==0:
            crr.append(brr[i]-arr[i])
        else:
            crr.append(brr[i]-max(brr[i-1],arr[i]))
    print(*crr)