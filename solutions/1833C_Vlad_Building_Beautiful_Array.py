a=int(input())
for _ in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    if min(arr)%2!=0:
        print("YES")
    else:
        odd=0
        even=0
        for i in arr:
            if i%2:
                odd+=1
            else:
                even+=1
        if odd==0 or even==0:
            print("YES")
        else:
            print("NO")