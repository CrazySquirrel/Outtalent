class Solution:
    def compress(self, chars: List[str]) -> int:
        result = []

        v, c = '', 0

        for char in chars:
            if v == char:
                c += 1
            else:
                result.append(v)
                if c > 1: result.append(str(c))
                v, c = char, 1

        result.append(v)
        if c > 1: result.append(str(c))

        result = ''.join(result)

        del chars[len(result):]

        for i in range(len(result)):
            chars[i] = result[i]

        return len(chars)
