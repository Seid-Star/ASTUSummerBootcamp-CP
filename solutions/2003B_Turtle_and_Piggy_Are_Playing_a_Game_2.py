a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    print(arr[b//2])