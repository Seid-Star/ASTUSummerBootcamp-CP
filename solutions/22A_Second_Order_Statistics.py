a=int(input())
arr=list(map(int,input().split()))
brr=list(set(arr))
brr.sort()
if len(brr)==1:
    print("NO")
else:
    print(brr[1])