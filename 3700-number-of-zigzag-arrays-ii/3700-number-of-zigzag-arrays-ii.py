class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        # Initial vector for length = 2
        # U[i] = arrays ending at value i with last move UP
        # D[i] = arrays ending at value i with last move DOWN
        size = 2 * m
        vec = [0] * size
        for i in range(m):
            vec[i] = i                  # previous value < i
            vec[m + i] = m - 1 - i      # previous value > i

        steps = n - 2
        if steps == 0:
            return sum(vec) % MOD

        # Transition matrix
        T = [[0] * size for _ in range(size)]

        # newU[x] = sum_{y < x} D[y]
        for x in range(m):
            row = x
            for y in range(x):
                T[row][m + y] = 1

        # newD[x] = sum_{y > x} U[y]
        for x in range(m):
            row = m + x
            for y in range(x + 1, m):
                T[row][y] = 1

        def mat_mul(A, B):
            n1, n2, n3 = len(A), len(B), len(B[0])
            C = [[0] * n3 for _ in range(n1)]
            for i in range(n1):
                Ai = A[i]
                Ci = C[i]
                for k in range(n2):
                    if Ai[k]:
                        aik = Ai[k]
                        Bk = B[k]
                        for j in range(n3):
                            Ci[j] = (Ci[j] + aik * Bk[j]) % MOD
            return C

        def mat_vec_mul(A, v):
            res = [0] * len(A)
            for i in range(len(A)):
                s = 0
                row = A[i]
                for j in range(len(v)):
                    if row[j]:
                        s = (s + row[j] * v[j]) % MOD
                res[i] = s
            return res

        # Binary exponentiation on matrix applied to vector
        M = T
        while steps:
            if steps & 1:
                vec = mat_vec_mul(M, vec)
            M = mat_mul(M, M)
            steps >>= 1

        return sum(vec) % MOD