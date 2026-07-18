a=int(input())
arr=list(map(int,input().split()))
b=arr.count(1)
brr=[]
for i in range(len(arr)):
    if arr[i]==1 and i!=0:
        brr.append(arr[i-1])
brr.append(arr[-1])
print(b)
print(*brr)