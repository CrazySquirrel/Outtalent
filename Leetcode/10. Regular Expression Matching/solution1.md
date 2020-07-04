# Recursion

If there were no stars (the * wildcard character for regular expressions), the problem would be easier - we simply check from left to right if each character of the text matches the pattern.

When a star is present, we may need to check many different suffixes of the text and see if they match the rest of the pattern. A recursive solution is a straightforward way to represent this relationship.

Without a star, our solution would look like this:

```python
def match(text, pattern):
    if not pattern: return not text
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    return first_match and match(text[1:], pattern[1:])
```

If a star is present in the pattern, it will be in the second position pattern[1]. Then, we may ignore this part of the pattern, or delete a matching character in the text. If we have a match on the remaining strings after any of these operations, then the initial inputs matched.

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        fm = s and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or fm and self.isMatch(s[1:], p)
        else:
            return fm and self.isMatch(s[1:], p[1:])
```

## Complexity Analysis

* Time Complexity: ![](1.png)

* Space Complexity: ![](1.png)

[Next](solution2.md)