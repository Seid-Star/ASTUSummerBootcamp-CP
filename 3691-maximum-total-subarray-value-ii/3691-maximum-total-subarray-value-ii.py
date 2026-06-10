from typing import List
from collections import deque

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def count_ge(v: int) -> int:
            if v <= 0:
                return n * (n + 1) // 2
            max_dq, min_dq = deque(), deque()
            cnt_lt = l = 0
            for r in range(n):
                while max_dq and nums[max_dq[-1]] <= nums[r]: max_dq.pop()
                max_dq.append(r)
                while min_dq and nums[min_dq[-1]] >= nums[r]: min_dq.pop()
                min_dq.append(r)
                while nums[max_dq[0]] - nums[min_dq[0]] >= v:
                    l += 1
                    if max_dq[0] < l: max_dq.popleft()
                    if min_dq[0] < l: min_dq.popleft()
                cnt_lt += r - l + 1
            return n * (n + 1) // 2 - cnt_lt

        def subarray_extreme_sum(use_max: bool) -> int:
            """Sum of subarray-max or subarray-min over ALL subarrays."""
            stack, total = [], 0
            for i in range(n):
                while stack:
                    top = stack[-1]
                    dominated = nums[top] <= nums[i] if use_max else nums[top] >= nums[i]
                    if dominated:
                        stack.pop()
                        left = stack[-1] if stack else -1
                        total += nums[top] * (top - left) * (i - top)
                    else:
                        break
                stack.append(i)
            while stack:
                top = stack.pop()
                left = stack[-1] if stack else -1
                total += nums[top] * (top - left) * (n - top)
            return total

        def sum_ge(v: int) -> int:
            """
            Sum of (max-min) over subarrays with max-min >= v.
            
            Strategy:
              sum_ge(v) = total_sum - sum_lt(v)
            
            For sum_lt(v): sliding window [l..r] stays valid (max-min < v).
            For each r, left-endpoints l..r all form valid subarrays.
            
            Track sum_max = Σ_{l'=l}^{r} max(nums[l'..r])
                  sum_min = Σ_{l'=l}^{r} min(nums[l'..r])
            
            Deque invariant: max_dq stores indices in decreasing value order.
            Each index j in max_dq is the max for left-endpoints in
              (prev_in_dq, j], i.e., span = j - prev  endpoints.
            But "prev" must be clamped to current l, so we track spans lazily:
              Instead of storing spans, recompute from deque positions + current l.
            
            On push r:  pop dominated backs, then
              sum_max += nums[r] * (r - (max_dq[-2] if len>1 else l-1))
                                        ^^^ this is wrong if l moved since last push
            
            ROOT CAUSE of previous bug: when l advances past intermediate deque
            elements, the "left boundary" of the front element is stale.
            
            FIX: Don't store spans implicitly via deque neighbor positions.
            Instead, store (index, left_boundary) pairs in the deque,
            updating left_boundary when l advances past an element.
            """
            if v <= 0:
                return subarray_extreme_sum(True) - subarray_extreme_sum(False)

            total_sum = subarray_extreme_sum(True) - subarray_extreme_sum(False)

            # Deque stores (index, left_bound) where left_bound is the leftmost
            # left-endpoint for which this element is the max/min.
            # Contribution to sum_max = nums[idx] * (idx - left_bound + 1)
            #   ... but left_bound changes as l advances. So store index only,
            #   and define left_bound(i) = max(l, prev_dq_element + 1).
            # On removal from left when l advances: just increment l and
            # recompute the front's effective span lazily.

            max_dq, min_dq = deque(), deque()  # indices only
            sum_max = sum_min = 0
            sum_lt = 0
            l = 0

            for r in range(n):
                # ---- Push r into max_dq ----
                # Pop elements from back that are <= nums[r] (they're dominated)
                while max_dq and nums[max_dq[-1]] <= nums[r]:
                    j = max_dq[-1]
                    # j was responsible for left-endpoints [effective_left(j)..j]
                    # effective_left(j) = max(l, prev+1) where prev = max_dq[-2] if exists
                    left_j = (max_dq[-2] + 1) if len(max_dq) >= 2 else l
                    sum_max -= nums[j] * (j - left_j + 1)
                    max_dq.pop()
                # Now push r
                left_r = (max_dq[-1] + 1) if max_dq else l
                sum_max += nums[r] * (r - left_r + 1)
                max_dq.append(r)

                # ---- Push r into min_dq ----
                while min_dq and nums[min_dq[-1]] >= nums[r]:
                    j = min_dq[-1]
                    left_j = (min_dq[-2] + 1) if len(min_dq) >= 2 else l
                    sum_min -= nums[j] * (j - left_j + 1)
                    min_dq.pop()
                left_r = (min_dq[-1] + 1) if min_dq else l
                sum_min += nums[r] * (r - left_r + 1)
                min_dq.append(r)

                # ---- Shrink from left while max - min >= v ----
                while max_dq and min_dq and \
                      nums[max_dq[0]] - nums[min_dq[0]] >= v:
                    # Remove left-endpoint l from both sum_max and sum_min.
                    # The front of max_dq owns endpoint l.
                    # Its effective span is [l .. max_dq[0]], count = max_dq[0] - l + 1.
                    # Removing l shrinks it by 1: sum_max -= nums[max_dq[0]] * 1
                    sum_max -= nums[max_dq[0]]
                    if max_dq[0] == l:
                        # This element no longer covers any endpoint → pop
                        # But only if the next element starts right at l+1
                        # Actually: after removing l, front covers [l+1..max_dq[0]]
                        # which is empty iff max_dq[0] == l
                        max_dq.popleft()

                    sum_min -= nums[min_dq[0]]
                    if min_dq[0] == l:
                        min_dq.popleft()

                    l += 1

                sum_lt += sum_max - sum_min

            return total_sum - sum_lt

        # Binary search: largest v where count_ge(v) >= k
        lo, hi = 0, max(nums) - min(nums)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if count_ge(mid) >= k:
                lo = mid
            else:
                hi = mid - 1

        v_star = lo
        cnt_above = count_ge(v_star + 1)
        above_sum = sum_ge(v_star + 1)
        take_at_vstar = k - cnt_above

        return above_sum + take_at_vstar * v_star