# Read from the file file.txt and print its transposed content to stdout.
columns=$(head -n 1 file.txt | wc -w)
for ((i = 1; i <= $columns; i++)); do
  cut -d' ' -f $i file.txt | sed -z 's/\n/ /g;s/ $/\n/'
done
