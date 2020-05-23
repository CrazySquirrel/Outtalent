class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        if len(digits) == 0: return []
        if len(digits) == 1: return list(phone[int(digits[0])])

        prev = self.letterCombinations(digits[:-1])
        suffix = list(phone[int(digits[-1])])

        return [j + i for j in prev for i in suffix]
