#!/usr/bin/env python2
import re
import sys

from cgminer_api import cgminer_api

pattern = re.compile(r'.*Ver\[(?P<ver>.+)\].*DNA')

def debug(ip):
    global pattern
    js = cgminer_api(ip, 4028, ['estats'])
    for estat in sorted(js['STATS'], key=lambda k: k['STATS']):
        for mm in sorted(estat):
            if mm[:5] == 'MM ID' and re.match(pattern, estat[mm]) is not None:
                g = re.match(pattern, estat[mm]).groupdict()
                print '[{:>13}][{:>2}][{:>2}]\tVer[{}]'.format(
                    ip, estat['ID'][3:], mm[5:], g['ver'])

if __name__ == '__main__':
    ip = sys.argv[1]
    try:
        port = int(sys.argv[2])
    except IndexError:
        port = 4028
    cgminer_api(ip, port, ['debug', 'D'])
    debug(ip)
    cgminer_api(ip, port, ['debug', 'D'])
