#!/usr/bin/env python3

import re
import sys
import fileinput
from datetime import datetime

if len(sys.argv) <= 1:
	print('Please tell me which license file(s) to update')
	sys.exit(1)

PATTERN = re.compile(r'^([Cc]opyright.+) ([0-9-]{4,9}) (.+)$')
NEW_YEAR = datetime.now().year

for line in fileinput.input(inplace=True):
	match = PATTERN.match(line)
	if match:
		sys.stdout.write(f'{match.group(1)} {match.group(2)[:4]}-{NEW_YEAR} {match.group(3)}\n')
	else:
		sys.stdout.write(line)
