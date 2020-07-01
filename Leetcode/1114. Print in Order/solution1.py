import threading


class Foo:
    def __init__(self):
        self.l2 = threading.Lock()
        self.l2.acquire()
        self.l3 = threading.Lock()
        self.l3.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.l2.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.l2.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.l3.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.l3.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
