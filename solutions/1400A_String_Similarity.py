a=int(input())
for x in range(a):
    b=int(input())
    c=input().strip()
    d=''
    for i in range(0,(2*b-1),2):
        d+=c[i]
    print(d)