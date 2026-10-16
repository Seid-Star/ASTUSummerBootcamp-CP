class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        a = len(nums)
        mod = 10**9 + 7

        arr = [0] * (4 * a)
        brr = [0] * (4 * a)
        crr = [0] * (4 * a)

        def push(node, l, r):
            if crr[node] == 0:
                return

            mid = (l + r) // 2
            for child, length in (
                (node * 2, mid - l + 1),
                (node * 2 + 1, r - mid)
            ):
                brr[child] += 2 * crr[node] * arr[child] + crr[node] * crr[node] * length
                arr[child] += crr[node] * length
                crr[child] += crr[node]

            crr[node] = 0

        def update(node, l, r, ql, qr):
            if ql > r or qr < l:
                return

            if ql <= l and r <= qr:
                brr[node] += 2 * arr[node] + (r - l + 1)
                arr[node] += r - l + 1
                crr[node] += 1
                return

            push(node, l, r)
            mid = (l + r) // 2

            update(node * 2, l, mid, ql, qr)
            update(node * 2 + 1, mid + 1, r, ql, qr)

            arr[node] = arr[node * 2] + arr[node * 2 + 1]
            brr[node] = brr[node * 2] + brr[node * 2 + 1]

        last = {}
        ans = 0

        for i in range(a):
            p = last.get(nums[i], -1)
            update(1, 0, a - 1, p + 1, i)
            last[nums[i]] = i

            ans = (ans + brr[1]) % mod

        return ans
        