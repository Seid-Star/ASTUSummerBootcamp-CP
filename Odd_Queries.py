a=int(input())
for x in range(a):
    b,c=map(int,input().split())
    arr=list(map(int,input().split()))
    k=sum(arr)
    pre=[0]
    for i in range(len(arr)):
        pre.append(pre[-1]+arr[i])
    for j in range(c):
        e,f,g=map(int,input().split())
        h=k-pre[f]-pre[e-1]
        i=h+(f-e+1)*g
        if i%2!=0:
            print("YES")
        else:
            print("NO")
