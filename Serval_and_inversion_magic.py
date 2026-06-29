a=int(input())
for x in range(a):
    b=int(input())
    c=input().strip()
    arr=[]
    l=0
    r=len(c)-1
    while l<r:
        if c[l]!=c[r]:
            arr.append(l)
        l+=1
        r-=1
    if len(arr)==0:
        print("Yes")
    else:
        if arr[-1]-arr[0]+1==len(arr):
            print("Yes")
        else:
            print("No")
