# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    s = 0

    def rand10(self):
        self.s += 7
        return 1 + ((rand7() + self.s) % 10)
