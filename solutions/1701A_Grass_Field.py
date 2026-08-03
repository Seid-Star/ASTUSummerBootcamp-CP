a=int(input())
for x in range(a):
    b,c=map(int,input().split())
    d,e=map(int,input().split())
    arr=[b,c,d,e]
    count=arr.count(1)
    if count==0:
        print(0)
    elif count==4:
        print(2)
    else:
        print(1)