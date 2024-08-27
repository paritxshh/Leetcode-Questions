class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        g = defaultdict(list)
        for (a, b), s in zip(edges, succProb):
            g[a].append((b, s))
            g[b].append((a, s))
        q = [(-1, start_node)]
        d = [0] * n
        d[start_node] = 1
        while q:
            w, u = heappop(q)
            w = -w
            if d[u] > w:
                continue
            for v, t in g[u]:
                if d[v] < d[u] * t:
                    d[v] = d[u] * t
                    heappush(q, (-d[v], v))
        return d[end_node]