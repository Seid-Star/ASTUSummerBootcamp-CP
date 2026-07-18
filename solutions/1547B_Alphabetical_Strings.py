t = int(input())
 
for _ in range(t):
    s = input().strip()
    
    n = len(s)
    ok = True
 
    for c in range(n - 1, -1, -1):
        ch = chr(ord('a') + c)
 
        if s[0] == ch:
            s = s[1:]
        elif s[-1] == ch:
            s = s[:-1]
        else:
            ok = False
            break
 
    print("YES" if ok else "NO")