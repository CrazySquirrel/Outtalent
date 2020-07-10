class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def dfs(board: str, hand: Counter) -> int:
            if board == '': return 0

            i = 0
            n = len(board)
            ans = inf

            while i < n:
                j = i + 1
                while j < n and board[j] == board[i]: j += 1

                inc = 3 - (j - i)

                if hand[board[i]] >= inc:
                    use = inc if inc >= 0 else 0
                    hand[board[i]] -= use
                    tmp = dfs(board[:i] + board[j:], hand)
                    if tmp >= 0: ans = min(ans, tmp + use)
                    hand[board[i]] += use

                i = j

            return ans if ans < inf else -1

        return dfs(board, collections.Counter(hand))
