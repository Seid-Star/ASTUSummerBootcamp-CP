a=int(input())
b=input()
c=['0']*10
l=0
r=len(c)-1
for i in b:
    if i=='L':
        id=c.index('0')
        c[id]='1'
    elif i=='R':
        id= 9-c[::-1].index('0')
        c[id]='1'
    else:
        c[int(i)]='0'
print("".join(c))