import re


class Solution:
    def checkForIPv4(self, IP: str) -> bool:
        parts = IP.split('.')
        try:
            return len(parts) == 4 and all(
                [part.isdigit() and (len(part) == 1 or part[0] != '0') and 0 <= int(part) <= 255 for part in parts])
        except ValueError:
            return False

    def checkForIPv6(self, IP: str) -> bool:
        parts = IP.split(':')
        try:
            return len(parts) == 8 and all(
                [re.match('^[0-9a-fA-F]{1,4}$', part) and 0 <= int(part, 16) <= 65535 for part in parts])
        except ValueError:
            return False

    def validIPAddress(self, IP: str) -> str:
        if ':' in IP:
            return 'IPv6' if self.checkForIPv6(IP) else 'Neither'
        else:
            return 'IPv4' if self.checkForIPv4(IP) else 'Neither'
