class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        phone = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        def backtrack(combination, next_digits):
            if not next_digits:
                output.append(combination)
            else:
                for letter in phone[int(next_digits[0])]:
                    backtrack(combination + letter, next_digits[1:])

        output = []
        backtrack("", digits)
        return output
