class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        while l < len(chars):
            r = l + 1
            while r < len(chars) and chars[l] == chars[r]: r += 1
            num = r - l
            for k in range(r - l, 1, -1): chars.pop(l)
            if num > 1:
                for i, v in enumerate(str(num)): chars.insert(l + i + 1, v)
                l += len(str(num))
            l += 1
        return len(chars)
