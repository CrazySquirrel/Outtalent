class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank.append(start)
        bank = set(bank)
        if end not in bank: return -1
        choices = {'A', 'C', 'G', 'T'}
        queue = [(start, 0)]
        visited = {start}
        front = 0
        while front < len(queue):
            gene, step = queue[front]
            if gene == end: return step
            for i in range(8):
                for choice in choices:
                    mutation = gene[:i] + choice + gene[i + 1:]
                    if mutation in bank and mutation not in visited:
                        queue.append((mutation, step + 1))
                        visited.add(mutation)
            front += 1
        return -1
