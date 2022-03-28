#!/usr/bin/env python3
from data import data as d
NULL_CHAR = chr(0)

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())
        print(report.encode())
write_report(chr(0xE0)+NULL_CHAR+chr(0x29)+NULL_CHAR*5)


write_report(NULL_CHAR*8)
write_report(chr(32)+NULL_CHAR+chr(4)+NULL_CHAR*5)
write_report(NULL_CHAR*2+chr(5)+NULL_CHAR*5)
write_report(NULL_CHAR*8)
write_report(chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5)
write_report(NULL_CHAR*2+chr(44)+NULL_CHAR*5)
write_report(chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5)
write_report(NULL_CHAR*8)
