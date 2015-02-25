./get.sh > ver.txt 2>/dev/null
cat ver.txt | awk -F "Ver" '{print $2}' | sort | uniq -c
