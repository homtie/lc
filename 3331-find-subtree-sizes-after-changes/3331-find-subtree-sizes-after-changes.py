
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_children = [[] for _ in range(n)]
        last = {}

        def dfs(u):
            c = s[u]
            old = last.get(c, -1)

            last[c] = u

            for v in children[u]:
                dfs(v)

            last[c] = old

        new_parent = parent[:]

        def build(u):
            c = s[u]
            old = last.get(c, -1)

            if old != -1:
                new_parent[u] = old

            last[c] = u

            for v in children[u]:
                build(v)

            last[c] = old

        build(0)

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        ans = [1] * n

        def count(u):
            for v in new_children[u]:
                count(v)
                ans[u] += ans[v]

        count(0)
        return ans
