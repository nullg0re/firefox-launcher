#!/usr/bin/python3
import sys, os, subprocess
import argparse
from colorama import Fore, Style

def cut_list(list_, n):
	for i in range(0, len(list_), n):
		yield list_[i:i +n]

def get_args():
	parser = argparse.ArgumentParser(description="Firefox Launcher")
	parser.add_argument('-f','--file',type=argparse.FileType('r'), help="List of urls", required=True)
	parser.add_argument('-n','--number',type=int,help='Number of urls to open congruently', required=True)

	args = parser.parse_args()

	file = args.file
	num = args.number

	return file, num

def main():
	file, num = get_args()

	print(Fore.GREEN+Style.BRIGHT+"[+] Launching URLs in Firefox now..."+Style.RESET_ALL)

	urls = []

	for line in file:
		urls.append('https://'+line.strip())

	print(Fore.GREEN+Style.BRIGHT+f"[+] Total URLs: {len(urls)}"+Style.RESET_ALL)

	count = 0
	for sublist in cut_list(urls, num):
		url_string = " ".join(sublist)
		subprocess.call('firefox %s' % str(url_string), shell=True)
		count += len(sublist)
		print(Fore.GREEN+Style.BRIGHT+f"[+] {len(urls) - count} URLs Remaining."+Style.RESET_ALL)

	print(Fore.GREEN+Style.BRIGHT+"[+] URLs have been launched. Exiting now...")
	exit(-1)

if __name__ == '__main__':
	main()
