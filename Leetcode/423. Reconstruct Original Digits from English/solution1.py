from collections import Counter, defaultdict


class Solution:
    def originalDigits(self, s: str) -> str:
        lookup = [('w', 'two', 2), ('x', 'six', 6), ('g', 'eight', 8), ('s', 'seven', 7), ('t', 'three', 3),
                  ('u', 'four', 4), ('v', 'five', 5), ('z', 'zero', 0), ('i', 'nine', 9), ('o', 'one', 1)]

        counter = Counter(s)
        result = defaultdict(int)

        for key, word, num in lookup:
            if key not in counter: continue
            result[num] += counter[key]
            for c in word: counter[c] -= result[num]

        return ''.join([str(n) * result[n] for n in range(10) if n in result])
