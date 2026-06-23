a=int(input())
for x in range(a):
    b=int(input())
    c=input()
    coun=0
    for i in range(b):
        d=c[i:]+c[:i]
        count=1
        for j in range(1,b):
            if d[j-1]!=d[j]:
                count+=1
        coun=max(coun,count)
    print(coun)
        
