import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = []
        busy = []
        ans = []

        for i in range(len(servers)):
            heapq.heappush(free, (servers[i], i))

        time = 0

        for i in range(len(tasks)):
            time = max(time, i)

            while busy and busy[0][0] <= time:
                a, b, c = heapq.heappop(busy)
                heapq.heappush(free, (b, c))

            if not free:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    a, b, c = heapq.heappop(busy)
                    heapq.heappush(free, (b, c))

            a, b = heapq.heappop(free)
            ans.append(b)

            heapq.heappush(busy, (time + tasks[i], a, b))

        return ans