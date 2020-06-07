class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-', '').upper()
        l = len(S)
        if l % K == 0:
            return '-'.join([S[i:i + K] for i in range(0, len(S), K)])
        else:
            return '-'.join([S[0:l % K]] + [S[i:i + K] for i in range(l % K, len(S), K)])
