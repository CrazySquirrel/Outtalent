class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        X = min(abs(len(s) - 6), abs(len(s) - 20)) if len(s) < 6 or len(s) > 20 else 0

        low = high = dig = 0
        for i in s:
            if ord(i) >= 97 and ord(i) <= 122: low = 1
            if ord(i) >= 65 and ord(i) <= 90: high = 1
            if ord(i) >= 48 and ord(i) <= 57: dig = 1
        Y = 3 - low - high - dig

        i, count, repeat = 0, 1, []

        while i <= len(s) - 2:
            if s[i + 1] == s[i]:
                count = count + 1
            else:
                if count >= 3: repeat.append(count)
                count = 1
            if i + 1 == len(s) - 1:
                if count >= 3: repeat.append(count)
                break
            i = i + 1

        Z = sum([m // 3 for m in repeat])

        if repeat: price = [m % 3 + 1 for m in repeat]

        if 6 <= len(s) <= 20: return max(Y, Z)
        if 6 > len(s): return max(X, Y, Z)

        tempX = X

        for i in range(len(repeat)):
            if tempX == 0: break
            if price[i] == 1:
                price[i] -= 1
                repeat[i] -= 1
                tempX -= 1

        for i in range(len(repeat)):
            if tempX <= 0: break
            if price[i] == 2:
                price[i] -= min(tempX, 2)
                repeat[i] -= min(tempX, 2)
                tempX -= 2

        for i in range(len(repeat)):
            if tempX <= 0: break
            if repeat[i] >= 2:
                temp = repeat[i] // 3
                repeat[i] -= min(X, temp * 3)
                tempX -= min(X, temp * 3)

        Z = sum([m // 3 for m in repeat])

        return X + max(Y, Z)
