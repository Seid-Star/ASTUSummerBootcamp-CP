a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    count=0
    for i in range(len(arr)):
        if arr[i]<=i+1:
            count+=1
    print(count)