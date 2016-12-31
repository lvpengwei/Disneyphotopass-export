#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import os
import binwalk

def dlfile(url, count):
	localpath = "image-download/%d" % (count)
	urllib.urlretrieve(url, localpath)

def main():
	# Download
	f = open("disneyphotopass")
	count = 0
	while 1:
		line = f.readline()
		if not line:
			break
		count = count + 1
		dlfile(line, count)

	print 'download done.'
	f.close()

	# Analysis
	for x in xrange(0, count):
		path = "image-download/%d" % (x + 1)
		for module in binwalk.scan(path, signature=True, quiet=True, extract=True):
			result = module.results[2]
			os.system("dd if=%s bs=1 skip=%d of=image/%d.jpg" % (path, result.offset, x + 1))

if __name__ == '__main__':
	main()
