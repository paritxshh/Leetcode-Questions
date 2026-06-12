class Solution:
    def assignEdgeWeights(self, edges, queries):
        MOD = 10**9 + 7

        n = len(edges) + 1
        LOG = 17

        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        depth = [0] * (n + 1)
        parent = [[-1] * (n + 1) for _ in range(LOG)]

        def dfs(u, p):
            parent[0][u] = p

            for v in graph[u]:
                if v == p:
                    continue
                depth[v] = depth[u] + 1
                dfs(v, u)

        dfs(1, -1)

        for j in range(1, LOG):
            for i in range(1, n + 1):
                if parent[j - 1][i] != -1:
                    parent[j][i] = parent[j - 1][parent[j - 1][i]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            for j in range(LOG):
                if diff & (1 << j):
                    u = parent[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if parent[j][u] != parent[j][v]:
                    u = parent[j][u]
                    v = parent[j][v]

            return parent[0][u]

        ans = []

        for u, v in queries:
            w = lca(u, v)

            k = depth[u] + depth[v] - 2 * depth[w]

            if k == 0:
                ans.append(0)
            else:
                ans.append(pow(2, k - 1, MOD))

        return ans