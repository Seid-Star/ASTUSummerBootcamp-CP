a=int(input())
arr=list(map(int,input().split()))
Min=10**9
N_Min=10**9
for i in arr:
    if i<Min:
        N_Min=Min
        Min=i
    elif Min<i<N_Min:
        N_Min=i
if N_Min==10**9:
    print("NO")
else:
    print(N_Min)
        
# brr=list(set(arr))
# brr.sort()
# if len(brr)==1:
#     print("NO")
# else:
#     print(brr[1])