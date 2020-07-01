class Foo:
    def __init__(self):
        self.flag2 = False
        self.flag3 = False

    def first(self, printFirst: 'Callable[[], None]') -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.flag2 = True

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.flag2 == False: time.sleep(0.01)
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.flag3 = True

    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.flag3 == False: time.sleep(0.01)
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
