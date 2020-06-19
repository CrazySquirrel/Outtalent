class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ws = set(wordList)

        if endWord not in ws: return 0

        bs = {beginWord}
        es = {endWord}

        lv = 1

        while bs:
            ws -= bs
            lv += 1
            t = set()

            for w in bs:
                for i in range(len(w)):
                    l = w[:i]
                    r = w[i + 1:]

                    for c in string.ascii_lowercase:
                        n = l + c + r

                        if n in ws:
                            if n in es:
                                return lv
                            else:
                                t.add(n)
            bs = t
            if len(bs) > len(es): bs, es = es, bs

        return 0
