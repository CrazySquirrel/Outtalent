class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dct = collections.defaultdict(list)

        for i, char in enumerate(s):
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    dct[l].append(r)
                    l -= 1
                    r += 1
                else:
                    break

            l, r = i, i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    dct[l].append(r)
                    l -= 1
                    r += 1
                else:
                    break

        result = []
        self.backtrack(0, [], dct, s, result)
        return result

    def backtrack(self, index, partition, dct, s, partitions):
        if index >= len(s):
            partitions.append(partition[:])
            return

        for end in dct[index]:
            partition.append(s[index:end + 1])
            self.backtrack(end + 1, partition, dct, s, partitions)
            partition.pop()

        return
