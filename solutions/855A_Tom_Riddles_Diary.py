a=int(input())
arr=[]
for x in range(a):
    b=input()
    if b in arr:
        print("YES")
    else:
        print("NO")
        arr.append(b)
 