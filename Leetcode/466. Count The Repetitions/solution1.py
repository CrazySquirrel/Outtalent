class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0: return 0

        pos = [0] * (len(s2) + 1)
        counter = [0] * (len(s2) + 1)

        index = 0
        count = 0

        for i in range(n1):
            for j in range(len(s1)):
                if s1[j] == s2[index]:
                    index += 1
                if index == len(s2):
                    index = 0
                    count += 1

            counter[i] = count
            pos[i] = index

            for k in range(i):
                if pos[k] == index:
                    pre_count = counter[k]
                    patten_count = (counter[i] - counter[k]) * ((n1 - 1 - k) // (i - k))
                    remain_count = counter[k + (n1 - 1 - k) % (i - k)] - counter[k]

                    return (pre_count + patten_count + remain_count) // n2

        return counter[n1 - 1] // n2
