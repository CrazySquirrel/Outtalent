class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict.sort(key=lambda x: len(x), reverse=True)

        @lru_cache(None)
        def dfs(s):
            if not s: return [""]
            res = []
            for word in wordDict:
                if s[:len(word)] != word: continue
                for r in dfs(s[len(word):]): res.append(word + ("" if not r else " " + r))
            return res

        return dfs(s)
