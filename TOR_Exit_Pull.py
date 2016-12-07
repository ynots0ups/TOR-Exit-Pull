#!/usr/bin/env python2.7

#################################################
#                                               #
#                TOR_Exit_Pull.py               #
#                     v1.0                      #
#                                               #
#             By s0ups (@ynots0ups)             #
#                                               #
#        https://github.com/ynots0ups/          #
#                                               #
#################################################
#
# All this shit does is dump a csv of current TOR
# exit nodes. That's it.
#

import re
import csv
import requests

#################################################
########### Shit For You To Change ##############

# Nothing. Get the fuck out of here. Fuck off.

#################################################
#################################################

regex = re.compile(r'ExitAddress ((?:[0-9]{1,3}\.){3}[0-9]{1,3})')
# Get messy list from TOR
request = requests.get('https://check.torproject.org/exit-addresses')
data = request.text
# Fix the mess
results = regex.findall(data)
# Output it as a csv
with open('TOR_Exit_Nodes.csv', 'wb') as ofile:
    wr = csv.writer(ofile)
    wr.writerow(results)
# EOF and stuff