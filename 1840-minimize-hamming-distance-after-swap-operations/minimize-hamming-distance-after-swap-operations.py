from collections import Counter

class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)

        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            a = find(a)
            b = find(b)

            if a != b:
                parent[b] = a

        # Connect indices
        for a, b in allowedSwaps:
            union(a, b)

        # Group source values
        groups = {}

        for i in range(n):
            root = find(i)

            if root not in groups:
                groups[root] = Counter()

            groups[root][source[i]] += 1

        # Calculate mismatches
        ans = 0

        for i in range(n):
            root = find(i)

            if groups[root][target[i]] > 0:
                groups[root][target[i]] -= 1
            else:
                ans += 1

        return ans
