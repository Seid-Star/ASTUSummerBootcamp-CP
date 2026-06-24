a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    brr=sorted(arr)
    for i in range(1,len(arr)-1,2):
        if brr[i]!=brr[i+1]:
            print("NO")
            break
    else:
        print("YES")
