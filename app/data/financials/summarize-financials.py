#!/usr/bin/env python

import sys
import csv
from decimal import Decimal as D

def addfunding(alldata, key, funding):

    if key in alldata:
        alldata[key] += funding
    else:
        alldata[key] = funding


    return alldata
   

def main(args):

    inputfilename = args[1]
    outputfile = args[2]

    years = []
    agencies = []
    cities = []
    industries = []

    alldata = {}

    # year ~ agency ~ locality ~ funding

    with open(inputfilename, 'rU') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')

        # 0 - year
        # 1 - agency
        # 2 - locality
        # 3 - funding
        # 4 - industry

        for row in csvreader:

            year = row['year']
            agency = row['agency']
            locality = row['locality']
            funding = D(row['funding'])
            industry = row['industry']

            fullkey = year + '~' + agency + '~' + locality
            allagencykey = year + '~ALL~' + locality
            alllocalitykey = year + '~' + agency + '~ALL'
            allagencylocalitykey = year + '~ALL~ALL'

            alldata = addfunding(alldata, fullkey, funding)
            alldata = addfunding(alldata, allagencykey, funding)
            alldata = addfunding(alldata, alllocalitykey, funding)
            alldata = addfunding(alldata, allagencylocalitykey, funding)

    for key in alldata.keys():
        keys = key.split('~')
        print ','.join(keys) + ',' + str(alldata[key])


if __name__ == '__main__':
    main(sys.argv)
