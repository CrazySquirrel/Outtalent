class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bfs = [(start, 0)]
        while bfs:
            gene, step = bfs.pop(0)
            if gene == end: return step
            for i in range(8):
                for x in "ACGT":
                    mutation = gene[:i] + x + gene[i + 1:]
                    if mutation in bank and mutation != gene:
                        bfs.append((mutation, step + 1))
                        bank.remove(mutation)
        return -1
