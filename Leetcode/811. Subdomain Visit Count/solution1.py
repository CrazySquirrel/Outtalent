class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        h = collections.Counter()

        for cpdomain in cpdomains:
            count, domain = cpdomain.split(' ')

            count = int(count)
            parts = domain.split('.')

            for i in range(len(parts)): h['.'.join(parts[i:])] += count

        return ['%d %s' % (h[k], k) for k in h]
