a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    print(arr[-1]-arr[0]+arr[-2]-arr[1])
