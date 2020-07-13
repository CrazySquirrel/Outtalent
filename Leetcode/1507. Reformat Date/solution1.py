class Solution:
    def reformatDate(self, date: str) -> str:
        d, m, y = date.split(' ')
        d = int(d[:-2])
        m = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"].index(m)
        y = int(y)
        return '%d-%02d-%02d' % (y, m + 1, d)
