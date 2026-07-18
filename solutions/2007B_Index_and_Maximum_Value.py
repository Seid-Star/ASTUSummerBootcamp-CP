a=int(input())
for x in range(a):
    b,c=map(int,input().split())
    arr=list(map(int,input().split()))
    brr=[]
    cur_max=max(arr)
    for i in range(c):
        e,f,g=input().split()
        f=int(f)
        g=int(g)
        if f<=cur_max<=g:
            if e=='+':
                cur_max=cur_max+1
            else:
                cur_max=cur_max-1
        brr.append(cur_max)
    print(*brr)
 