# Word counter

## Algorithm

* Count how many of each word in words and save result to words_counter
* Count how many words and save result to words_count
* Save word length to word_len
* Save s length to s_len
* Iterate i from 0 to (s_len - word_len * words_count + 1):
    * Create empty Counter
    * Iterate j from 0 to words_count:
        * Set k = i + j * word_len
        * Get s_word from s[k:k + word_len]
        * Count s_word
        * If h[word] > words_counter[word] then break
    * If we iterate through from 0 to words_count without break add i to result
* Return result

```python
from collections import Counter, defaultdict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: return []
        if not all([word in s for word in words]): return []

        words_counter = Counter(words)
        words_count = len(words)
        word_len = len(words[0])
        s_len = len(s)

        result = []

        for i in range(s_len - word_len * words_count + 1):
            h = defaultdict(int)

            for j in range(words_count):
                k = i + j * word_len
                word = s[k:k + word_len]
                h[word] += 1

                if h[word] > words_counter[word]: break
            else:
                result.append(i)

        return result
```

## Complexity Analysis:

* Time complexity: O(N – K) * K

* Space Complexity: O(N)

Where N is th length of S and K total length of all words

[Prev](solution1.md)