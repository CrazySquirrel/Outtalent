import re

IPv4 = re.compile('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$')
IPv6 = re.compile('^((([0-9A-Fa-f]{1,4}:){1,6}:)|(([0-9A-Fa-f]{1,4}:){7}))([0-9A-Fa-f]{1,4})$')

class Solution:
    def validIPAddress(self, IP: str) -> str:
        if IPv4.match(IP): return 'IPv4'
        if IPv6.match(IP): return 'IPv6'
        return 'Neither'