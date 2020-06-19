class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        counter = collections.Counter()
        for word in A.split(): counter[word] += 1
        for word in B.split(): counter[word] += 1
        return [word for word in counter if counter[word] == 1]
