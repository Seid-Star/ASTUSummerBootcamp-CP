t = int(input())
 
for _ in range(t):
    s = input()
 
    for i in range(1, len(s)):
        a = s[:i]
        b = s[i:]
 
        if a[0] != '0' and b[0] != '0' and int(a) < int(b):
            print(a, b)
            break
    else:
        print(-1)