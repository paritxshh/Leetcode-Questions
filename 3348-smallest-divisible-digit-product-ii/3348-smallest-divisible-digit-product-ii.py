import math

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp = t
        counts = [0, 0, 0, 0]
        for i, p in enumerate([2, 3, 5, 7]):
            while temp % p == 0:
                counts[i] += 1
                temp //= p
                
        if temp > 1:
            return "-1"
            
        divs = []
        for a in range(counts[0] + 1):
            for b in range(counts[1] + 1):
                for c in range(counts[2] + 1):
                    for d in range(counts[3] + 1):
                        divs.append((2**a) * (3**b) * (5**c) * (7**d))
        divs.sort()
        
        trans = {v: [v] * 10 for v in divs}
        for v in divs:
            for d in range(1, 10):
                trans[v][d] = v // math.gcd(v, d)
                
        dp = {v: float('inf') for v in divs}
        dp[1] = 0
        
        for v in divs:
            if v == 1:
                continue
            best = float('inf')
            for d in range(2, 10):
                nxt = trans[v][d]
                if dp[nxt] + 1 < best:
                    best = dp[nxt] + 1
            dp[v] = best
            
        n = len(num)
        first_zero = num.find('0')
        
        if first_zero == -1:
            max_i_allowed = n - 1
        else:
            max_i_allowed = first_zero
            
        prefix_t = [t]
        for i in range(max_i_allowed):
            prefix_t.append(trans[prefix_t[-1]][int(num[i])])
            
        if first_zero == -1:
            full_t = trans[prefix_t[-1]][int(num[-1])]
            if full_t == 1:
                return num
                
        for i in range(max_i_allowed, -1, -1):
            p_t = prefix_t[i]
            rem = n - 1 - i
            
            for d in range(int(num[i]) + 1, 10):
                t_req = trans[p_t][d]
                if dp[t_req] <= rem:
                    ans = [num[:i], str(d)]
                    curr_t = t_req
                    for step in range(rem):
                        for nxt_d in range(1, 10):
                            next_t = trans[curr_t][nxt_d]
                            if dp[next_t] <= rem - 1 - step:
                                ans.append(str(nxt_d))
                                curr_t = next_t
                                break
                    return "".join(ans)
                    
        length = max(n + 1, dp[t])
        ans = []
        curr_t = t
        for step in range(length):
            for nxt_d in range(1, 10):
                next_t = trans[curr_t][nxt_d]
                if dp[next_t] <= length - 1 - step:
                    ans.append(str(nxt_d))
                    curr_t = next_t
                    break
        return "".join(ans)