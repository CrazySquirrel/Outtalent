class Codec:
    def __init__(self):
        self.urls = {}
        self.prefix = 'http://tinyurl.com/'
        self.counter = 0

    def encode(self, longUrl: str) -> str:
        self.counter += 1
        shortUrl = self.prefix + str(self.counter)
        self.urls[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        return self.urls.get(shortUrl, '')

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))