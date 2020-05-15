class Codec:
    def __init__(self):
        self.urls = []
        self.prefix = 'http://tinyurl.com/'
        self.prefix_length = len(self.prefix)
        self.counter = 0

    def encode(self, longUrl: str) -> str:
        self.counter += 1
        while len(self.urls) <= self.counter: self.urls.append('')
        self.urls[self.counter] = longUrl
        return self.prefix + str(self.counter)

    def decode(self, shortUrl: str) -> str:
        counter = int(shortUrl[self.prefix_length:])
        while len(self.urls) <= counter: self.urls.append('')
        return self.urls[counter]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))