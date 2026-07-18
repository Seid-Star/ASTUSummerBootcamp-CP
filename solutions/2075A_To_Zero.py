a=int(input())
for x in range(a):
    b,c=map(int,input().split())
    if b%2==0:
        if b%(c-1)==0:
            print(b//(c-1))
        else:
            print(b//(c-1)+1)
    else:
        if b-c==0:
            print(1)
        else:
            d=b-c
            if d%(c-1)==0:
                print(d//(c-1)+1)
            else:
                print(d//(c-1)+2)
                