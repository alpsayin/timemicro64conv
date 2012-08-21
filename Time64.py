#!/usr/bin/env python

from dateutil.relativedelta import relativedelta
from datetime import datetime
from optparse import OptionParser
import os
import re

if (__name__ == "__main__"):
	parser = OptionParser()
	parser.add_option("-i","--input", dest="inputTime", help="input time in 64 bit microseconds since 1 january 0 ad 00:00:00.000", type="int", metavar="MICROSECONDS")
	parser.add_option("-f","--file", dest="inputFile", help="input file to be renamed", metavar="FILE")
	(option, args) = parser.parse_args()
	# print args
	microseconds=option.inputTime
	microseconds=63513828028326875
	filename=option.inputFile
	if(microseconds is not None):
		beginning = datetime(1, 1, 1)
		output = beginning+relativedelta( microseconds=microseconds)
		output = output+relativedelta( years=-1, days=-13)
		print output.strftime("%I.%M %p %A %d, %B %Y")
	if(filename is not None):
		print filename
		pattern = re.compile(r'(.+)_(\d+)(\S+)')
		result = pattern.search(filename).groups()
		print result
		microseconds=int(result[1])
		beginning = datetime(1, 1, 1)
		output = beginning+relativedelta( microseconds=microseconds)
		output = output+relativedelta( years=-1, days=-13)
		newFilename = str(result[0]) + '_' + str(output.strftime("%I.%M %p %A %d, %B %Y")) + str(result[2])
		print newFilename
		os.renames(filename, newFilename)