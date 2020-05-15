import random
import string


class Codec:
    def __init__(self):
        self.urls = {}

    def encode(self, longUrl: str) -> str:
        suffix = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(6)])
        shortUrl = 'http://tinyurl.com/' + suffix
        self.urls[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        return self.urls.get(shortUrl, '')

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
