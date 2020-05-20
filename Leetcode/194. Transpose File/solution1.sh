# Read from the file file.txt and print its transposed content to stdout.
awk '
NR == 1 { for (i = 1; i <= NF; i++) { line[i] = $i } }
NR > 1 { for (i = 1; i <= NF; i++) { line[i] = line[i] " " $i } }
END { for (i = 1; i <= NF; i++) { print line[i] } }
' file.txt
