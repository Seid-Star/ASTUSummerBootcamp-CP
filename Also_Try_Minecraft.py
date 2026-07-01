a,b=map(int,input().split())
arr=list(map(int,input().split()))
pre=[0]*len(arr)
for j in range(1,len(arr)):
    pre[j]=pre[j-1]
    if arr[j]<arr[j-1]:
        pre[j]+=(arr[j-1]-arr[j])
pref=[0]*len(arr)
for i in range(len(arr)-2,-1,-1):
    pref[i]=pref[i+1]
    if arr[i]<arr[i+1]:
        pref[i]+= arr[i+1]-arr[i]
for x in range(b):
    c,d=map(int,input().split())
    e=c-1
    f=d-1
    if e<f:
        print(pre[f]-pre[e])
    else:
        print(pref[f]-pref[e])
