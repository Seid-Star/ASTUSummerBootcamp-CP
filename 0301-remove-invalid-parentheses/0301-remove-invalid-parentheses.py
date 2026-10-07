class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        def valid(s):
            count = 0

            for c in s:
                if c == '(':
                    count += 1

                elif c == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = [s]
        visited = {s}
        answer = []

        found = False

        while queue:

            current = queue.pop(0)

            if valid(current):
                answer.append(current)
                found = True

            if found:
                continue

            for i in range(len(current)):

                if current[i] != '(' and current[i] != ')':
                    continue

                new_string = current[:i] + current[i + 1:]

                if new_string not in visited:
                    visited.add(new_string)
                    queue.append(new_string)

        return answer