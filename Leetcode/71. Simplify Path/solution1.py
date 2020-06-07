class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dirs = path.split('/')
        for dir in dirs:
            if not dir or dir == '.': continue
            if dir == '..':
                if stack: stack.pop()
            else:
                stack.append(dir)
        return '/' + '/'.join(stack)
