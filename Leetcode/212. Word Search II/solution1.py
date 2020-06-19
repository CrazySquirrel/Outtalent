import re


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(i, j, parent):
            letter = board[i][j]

            node = parent[letter]

            if '$' in node:
                ret.append(node.pop('$'))

            board[i][j] = ''

            i > 0 and board[i - 1][j] in node and dfs(i - 1, j, node)
            j + 1 < n and board[i][j + 1] in node and dfs(i, j + 1, node)
            i + 1 < m and board[i + 1][j] in node and dfs(i + 1, j, node)
            j > 0 and board[i][j - 1] in node and dfs(i, j - 1, node)

            board[i][j] = letter

            if not node:
                parent.pop(letter)

        alphabet = ''.join({''.join(row) for row in board})
        match = re.compile('[' + alphabet + ']{1,}').fullmatch

        words = {word.strip() for word in words if match(word)}

        root = {}

        for word in words:
            curr = root

            for letter in word:
                if letter not in curr:
                    curr[letter] = {}

                curr = curr[letter]
            curr['$'] = word

        ret = []
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    dfs(i, j, root)

        return ret
