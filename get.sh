#!/bin/bash
for i in `seq 20 34`
do
	python debug.py 192.168.1.$i
done

python debug.py 192.168.1.100
python debug.py 192.168.1.101
