class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        queries_frequency = [query.count(min(query)) for query in queries]
        words_frequency = [word.count(min(word)) for word in words]
        return [sum(q < w for w in words_frequency) for q in queries_frequency]
