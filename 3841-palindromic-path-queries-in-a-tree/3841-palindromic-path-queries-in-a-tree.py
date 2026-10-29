class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        arr = [[] for i in range(n)]

        for u, v in edges:
            arr[u].append(v)
            arr[v].append(u)

        b = n.bit_length()
        par = [[0] * n for i in range(b)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        pref = [0] * n
        time = 0

        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                tin[u] = time
                time += 1

                if p == -1:
                    pref[u] = 1 << (ord(s[u]) - ord('a'))
                else:
                    pref[u] = pref[p] ^ (1 << (ord(s[u]) - ord('a')))

                par[0][u] = u if p == -1 else p

                for i in range(1, b):
                    par[i][u] = par[i - 1][par[i - 1][u]]

                stack.append((u, p, 1))

                for v in arr[u]:
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))

            else:
                tout[u] = time - 1

        bit = [0] * (n + 2)

        def update(i, val):
            i += 1
            while i <= n + 1:
                bit[i] ^= val
                i += i & -i

        def get(i):
            i += 1
            val = 0
            while i > 0:
                val ^= bit[i]
                i -= i & -i
            return val

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            d = depth[u] - depth[v]

            for i in range(b):
                if d & (1 << i):
                    u = par[i][u]

            if u == v:
                return u

            for i in range(b - 1, -1, -1):
                if par[i][u] != par[i][v]:
                    u = par[i][u]
                    v = par[i][v]

            return par[0][u]

        def pathmask(u, v, chars):
            w = lca(u, v)

            x = pref[u] ^ get(tin[u])
            y = pref[v] ^ get(tin[v])
            z = 1 << (ord(chars[w]) - ord('a'))

            return x ^ y ^ z

        chars = list(s)
        answer = []

        for q in queries:
            arrq = q.split()

            if arrq[0] == "update":
                u = int(arrq[1])
                c = arrq[2]

                old = 1 << (ord(chars[u]) - ord('a'))
                new = 1 << (ord(c) - ord('a'))

                if old != new:
                    change = old ^ new
                    update(tin[u], change)
                    update(tout[u] + 1, change)
                    chars[u] = c

            else:
                u = int(arrq[1])
                v = int(arrq[2])

                mask = pathmask(u, v, chars)
                answer.append(mask == 0 or (mask & (mask - 1)) == 0)

        return answer