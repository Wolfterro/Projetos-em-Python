#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
The MIT License (MIT)

Copyright (c) 2016 Wolfgang Almeida <wolfgang.almeida@yahoo.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from __future__ import print_function
from urllib2 import urlparse
from time import sleep

import os
import re
import sys
import json
import urllib2

# Changing default encoding
# =========================
reload(sys)
sys.setdefaultencoding('utf-8')

# Checking type of GET
# ====================
def checkGetType(numbers):
	sizeNum = len(numbers)

	typeCount = 0
	
	for x in range(sizeNum - 1, -1, -1):
		if numbers[x] == numbers[x - 1]:
			typeCount += 1
		else:
			break

	if typeCount == 1:
		return "Dubs"
	elif typeCount == 2:
		return "Trips"
	elif typeCount == 3:
		return "Quads"
	elif typeCount == 4:
		return "Quints"
	elif typeCount == 5:
		return "Sexts"
	elif typeCount == 6:
		return "Septs"
	elif typeCount == 7:
		return "Octs"
	elif typeCount == 8:
		return "Nons"
	elif typeCount >= 9:
		return "KEK HIMSELF!"
	else:
		return "N/A"

# Checking post numbers
# =====================
def checkPostNumbers(postNumbers):
	totalCount = 0

	dubs = 0
	trips = 0 
	quads = 0
	quints = 0
	sexts = 0
	septs = 0
	octs = 0
	nons = 0

	for numbers in postNumbers:
		lastNumber = numbers[len(numbers) - 1]
		lastButOneNumber = numbers[len(numbers) - 2]

		if lastNumber == lastButOneNumber:
			getType = checkGetType(numbers)
			print("Post No.%s - Check'd - (%s)" % (numbers, getType))
			sleep(0.10)
			
			totalCount += 1

			if getType == "Dubs":
				dubs += 1
			elif getType == "Trips":
				trips += 1
			elif getType == "Quads":
				quads += 1
			elif getType == "Quints":
				quints += 1
			elif getType == "Sexts":
				sexts += 1
			elif getType == "Septs":
				septs += 1
			elif getType == "Octs":
				octs += 1
			elif getType == "Nons":
				nons +=1
		else:
			print("Post No.%s" % (numbers))
			sleep(0.10)

	print("\n-----------------------------")
	print("[Check'em] Times check'd: %d" % (totalCount))
	print("[Check'em] Dubs: %d" % (dubs))
	print("[Check'em] Trips: %d" % (trips))
	print("[Check'em] Quads: %d" % (quads))
	print("[Check'em] Quints: %d" % (quints))
	print("[Check'em] Sexts: %d" % (sexts))
	print("[Check'em] Septs: %d" % (septs))
	print("[Check'em] Octs: %d" % (octs))
	print("[Check'em] Nons: %d" % (nons))

# Getting the post numbers from the thread
# ========================================
def getThreadPostNumbers(getPosts):
	postNumbers = []
	for posts in getPosts:
		if 'no' in posts:
			postNumbers.append(str(posts['no']))

	return postNumbers

# Getting the JSON file from the thread
# =====================================
def getThreadJSON(apiURL):
	try:
		response = urllib2.urlopen(apiURL)
		data = json.loads(response.read())
	except Exception as e:
		print("Error! Could not get JSON file!")
		print("Error: %s" % (e))
		sys.exit(1)
	
	return data['posts']

# Getting the thread URL from the user
# ====================================
def getBoardAndThread(threadURL):
	if threadURL == None:
		threadURL = raw_input("[Check'em] Insert the thread's URL: ")
		print("")

	url_split = urlparse.urlsplit(threadURL)

	if str(url_split[1]) != "boards.4chan.org" and str(url_split[1]) != "4chan.org":
		print("[Check'em] Very funny retard, wrong website!")
		sys.exit(1)
	else:
		toParse = str(url_split[2])
		board = toParse.split("/")[1]
		threadID = toParse.split("/")[3]
		
		return "https://a.4cdn.org/%s/thread/%s.json" % (board, threadID)

# Main Method
# ===========
def main():
	argc = len(sys.argv)
	version = "1.0"

	print("======================")
	print("Check'em - Version %s" % (version))
	print("======================\n")

	if argc >= 2:
		if str(sys.argv[1]) == "-u" or str(sys.argv[1]) == "--url":
			threadURL = str(sys.argv[2])
		else:
			threadURL = None
	else:
		threadURL = None

	apiURL = getBoardAndThread(threadURL)
	getPosts = getThreadJSON(apiURL)
	postNumbers = getThreadPostNumbers(getPosts)

	print("[Check'em] It's time to check'em!")
	print("---------------------------------")
	checkPostNumbers(postNumbers)

if __name__ == "__main__":
	main()