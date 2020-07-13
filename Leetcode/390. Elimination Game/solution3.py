class Solution:
    def lastRemaining(self, n: int) -> int:
        left = True
        head = step = 1
        while n > 1:
            if left or n % 2: head += step
            n //= 2
            step *= 2
            left = not left
        return head
