class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = Counter(s1.split()) + Counter(s2.split())
        return [s for s, v in count.items() if v == 1]