a=int(input())
for x in range(a):
    b,c=map(int,input().split())
    for i in range(b):
        arr=[]
        for j in range(c):
            if i%2==0:
                if j%2==0:
                    arr.append(1)
                else:
                    arr.append(0)
            else:
                if j%2==0:
                    arr.append(0)
                else:
                    arr.append(1)
            if (i//2+j//2)%2==1:
                arr[-1]=1-arr[-1]
        print(*arr)
