a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    if max(arr)==100:
        print("Yes")
    else:
        print("No")
