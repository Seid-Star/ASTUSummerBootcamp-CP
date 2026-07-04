a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    brr=[]
    count=0
    Max=10**10
    i=0
    while i<len(arr):
        count+=arr[i]
        Max=min(Max,count//(i+1))
        brr.append(Max)
        i+=1
    print(*brr)
