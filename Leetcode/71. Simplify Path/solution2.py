class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split('/'):
            if p not in {'', '.', '..'}:
                stack.append(p)
            elif p == '..' and stack:
                stack.pop()
        return '/' + '/'.join(stack)
