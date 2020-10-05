class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        lines_count = 1
        last_line_width = 0

        for c in S:
            cl = widths[ord(c) - 97]
            last_line_width += cl

            if last_line_width > 100:
                lines_count += 1
                last_line_width = cl

        return [lines_count, last_line_width]
