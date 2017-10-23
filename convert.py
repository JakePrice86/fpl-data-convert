#!/usr/bin/env python
#
# Very simple pyton file to convert FPL data to 
# useable CSV format.
#
# How to use:
#
# 	1. Download https://fantasy.premierleague.com/drf/elements/ to data.json
#	2. What fields do you want? Put them in the headers list
#	3. Run this file: $ python convert.py
#	4. Output file is output.csv - open in spreadsheet prog of choice
#
# @jakelprice - Oct 17
#
import csv
import json

final = []

with open('data.json') as data_file:
	data = json.load(data_file)

# Create Headers
headers = ['first_name', 'second_name', 'team', 'now_cost', 'total_points', 'form']
final.append(headers)

for line in data:
	# Create data we need
	sub = []
	for h in headers:
		d = line[h]
		# Check for int values, as we need to strip funny accents
		# due to excel limitations
		if (type(d) == int):
			sub.append(line[h])
		else:
			sub.append(line[h].encode('utf-8'))			
	# Add to main data
	final.append(sub)

# Write data output
with open('output.csv', "wb") as csv_file:
	writer = csv.writer(csv_file, delimiter=',')
	for line in final:
		writer.writerow(line)

print len(final)
