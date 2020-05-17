class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        mn = [-1] * 26
        mx = [-1] * 26
        intervals = []
        for i in range(len(S)):
            c = ord(S[i]) - 97
            if mn[c] == -1:
                mn[c] = i
                mx[c] = i
                intervals.append(c)
            else:
                mx[c] = i
        ans = []
        start = mn[intervals[0]]
        end = mx[intervals[0]]
        for interval in intervals:
            if end < mn[interval]:
                ans.append(end - start + 1)
                start = mn[interval]
                end = mx[interval]
            else:
                end = max(end, mx[interval])
        ans.append(end - start + 1)
        return ans
