a,b=map(int,input().split())
arr=list(map(int,input().split()))
brr=[0]+arr
crr=[0]*(a+1)
drr=[0]*(a+1)
for i in range(1,a):
    crr[i+1]=crr[i]+max(0,brr[i]-brr[i+1])
for i in range(a,1,-1):
    drr[i-1]=drr[i]+max(0,brr[i]-brr[i-1])
for i in range(b):
    c,d=map(int,input().split())
    if c<d:
        print(crr[d]-crr[c])
    else:
        print(drr[d]-drr[c])
