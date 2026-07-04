a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    found= False
    for j in range(1,b-1):
        i=j-1
        while i>=0 and arr[i]>=arr[j]:
            i-=1
        k=j+1
        while k<b and arr[k]>=arr[j]:
            k+=1
        if i>=0 and k<b:
            print("YES")
            print(i+1,j+1,k+1)
            found=True
            break
    if not found:
        print("NO")
