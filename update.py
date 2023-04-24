#!/usr/bin/env python3

import os
import re
import sys
import fileinput
import argparse
from datetime import datetime

parser = argparse.ArgumentParser(
	usage='%(prog)s [OPTION]',
	description='Updates license file(s) to the current year.'
)

parser.add_argument('-f', '--files', help='Multiline string of file paths', required=True)
args = parser.parse_args()

paths = []
for line in iter(args.files.splitlines()):
	if line != '':
		if not os.path.isfile(line):
			print(f'file not found at path "{line}"')
			sys.exit(1)
		elif line in paths:
			print(f'duplicate path "{line}"')
			sys.exit(1)
		else:
			paths.append(line)

PATTERN = re.compile(r'^([Cc]opyright.+) ([0-9-]{4,9}) (.+)$')
NEW_YEAR = datetime.now().year

for line in fileinput.input(files=paths, inplace=True):
	match = PATTERN.match(line)
	if match:
		sys.stdout.write(f'{match.group(1)} {match.group(2)[:4]}-{NEW_YEAR} {match.group(3)}\n')
	else:
		sys.stdout.write(line)
