from itertools import combinations


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.generator = combinations(characters, combinationLength)
        self.value = next(self.generator, None)

    def next(self) -> str:
        result = self.value
        self.value = next(self.generator, None)
        return ''.join(result)

    def hasNext(self) -> bool:
        return self.value is not None

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
