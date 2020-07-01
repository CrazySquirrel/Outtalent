class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        arr = ' '.join(words)
        ans = [i for i in words if arr.count(i) >= 2]
        return ans
