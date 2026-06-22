a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    c=arr[-1]-arr[0]+1
    d=c//2
    print(d)