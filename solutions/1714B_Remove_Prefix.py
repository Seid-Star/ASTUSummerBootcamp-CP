# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split())) 
#     seen = set()
#     count = 0
#     for i in range(n - 1, -1, -1):
#         if arr[i] in seen:
#             count = i + 1
#             break
#         seen.add(arr[i])   
#     print(count)
 
a=int(input()) 
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    brr=set()
    r=len(arr)-1
    while r>=0:
        if arr[r] in brr:
            break
        brr.add(arr[r])
        r-=1
    print(r+1)