class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def helper(live):
            ctr = collections.Counter((I, J)
                                      for i, j in live
                                      for I in range(i - 1, i + 2)
                                      for J in range(j - 1, j + 2)
                                      if I != i or J != j)

            return {ij for ij in ctr if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}

        live = helper({(i, j) for i, r in enumerate(board) for j, c in enumerate(r) if c})

        for i, row in enumerate(board):
            for j in range(len(row)):
                row[j] = int((i, j) in live)
