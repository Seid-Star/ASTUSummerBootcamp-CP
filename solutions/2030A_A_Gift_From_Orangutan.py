a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    c=max(arr)
    d=min(arr)
    e=len(arr)-1
    f=c-d
    print(f*e)