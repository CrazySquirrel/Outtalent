class Solution:
    def justifyString(self, word_list: List[str], maxWidth: int) -> str:
        if len(' '.join(word_list)) == maxWidth: return ' '.join(word_list)
        if len(word_list) == 1: return word_list[0] + ' ' * (maxWidth - len(word_list[0]))
        if len(word_list) == 2: return word_list[0] + ' ' * (maxWidth - len(word_list[0]) - len(word_list[1])) + word_list[1]
        lencur = len(''.join(word_list))
        len_spaces = maxWidth - lencur
        index = 0
        while len_spaces > 0:
            if index >= len(word_list) - 1: index = 0
            word_list[index] += ' '
            index += 1
            len_spaces -= 1
        return ''.join(word_list)

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        if not words: return []

        result = [[0, []]]

        for word in words:
            if result[-1][0] + len(word) > maxWidth: result.append([0, []])

            result[-1][0] += len(word) + 1
            result[-1][1].append(word)

        result[-1] = ' '.join(result[-1][1]) + ' ' * (maxWidth - result[-1][0] + 1)

        for i in range(len(result) - 1):
            result[i] = self.justifyString(result[i][1], maxWidth)

        return result
