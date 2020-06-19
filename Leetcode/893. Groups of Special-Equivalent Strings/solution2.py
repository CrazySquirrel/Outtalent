class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        def count(A):
            ans = [0] * 52
            for i, letter in enumerate(A): ans[ord(letter) - 97 + 26 * (i % 2)] += 1
            return tuple(ans)

        return len({count(word) for word in A})
