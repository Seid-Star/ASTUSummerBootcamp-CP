a = int(input())
 
for _ in range(a):
    b = input()
    ans = []
 
    for i in b:
        if i == 'T':
            ans.append(i)
 
    for i in b:
        if i != 'T':
            ans.append(i)
 
    print("".join(ans))