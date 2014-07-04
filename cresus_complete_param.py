#!/usr/bin/python
# -*- coding: utf8 -*-

from optparse import OptionParser

parser = OptionParser()

parser.add_option("-f", "--file", dest="file", help="file to convert")

(options, args) = parser.parse_args()

infile = options.file

extList = []
cnt = 0
nextprint = 0
cresusfile = infile
cresusnew = cresusfile.replace('Export', 'Import')
nextname = nextdebit = nextcredit = False
infile = open(cresusfile, 'r')
nfile = open(cresusnew, 'w')
lines = infile.readlines()
for line in lines:
    if nextname:
        curname = line[:line.find(' ')].strip().rstrip('.')
    if line.find('#') > -1:
        nextprint = 0
    if line.find('#NAME') > -1:
        nextname = True
    else:
        nextname = False
    if nextdebit:
        line = curname + '\n'
        nextdebit = False
    if line.find('#DEBIT') > -1:
        nextdebit = True
    else:
        nextdebit = False
    if nextcredit:
        line = curname + '\n'
        nextcredit = False
    if line.find('#CREDIT') > -1:
        nextcredit = True
    else:
        nextcredit = False
    if nextprint < 2:
        nfile.write(line)
        nextprint += 1
nfile.close()
infile.close()
print "END, new file %s is ready" % cresusnew
