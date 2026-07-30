a,b=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
pref=[arr[0]]
for i in arr[1:]:
    pref.append(pref[-1]+i)
for i in range(b):
    c,d=map(int,input().split())
    e=a-c
    f=e+d-1
    if e==0:
        print(pref[f])
    else:
        print(pref[f]-pref[e-1])
