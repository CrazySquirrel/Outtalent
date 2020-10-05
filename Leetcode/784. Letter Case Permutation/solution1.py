class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        result = []

        def dfs(i, prefix):
            if i >= len(S):
                result.append(''.join(prefix))
            elif S[i].isnumeric():
                prefix.append(S[i])
                dfs(i + 1, prefix)
                prefix.pop()
            else:
                prefix.append(S[i].upper())
                dfs(i + 1, prefix)
                prefix.pop()
                prefix.append(S[i].lower())
                dfs(i + 1, prefix)
                prefix.pop()

        dfs(0, [])

        return result
