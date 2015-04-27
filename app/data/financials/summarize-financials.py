#!/usr/bin/env python

import sys
import csv
from decimal import Decimal as D

import pprint

pp = pprint.PrettyPrinter(indent=4)

def addfunding(alldata, key, funding):

    if key in alldata:
        print "adding " + str(funding) + " for key " + key + " to " + str(alldata[key])
        alldata[key] += funding
    else:
        print "inserting " + str(funding) + " as new entry for " + key
        alldata[key] = funding

    return alldata

def generateCombinations(alldata, year, agency, locality, funding, industry):
   
    # all options selected by user, used by choropleth and bar chart
    fullkey = year + '~' + agency + '~' + locality + '~' + industry
    
    # options to draw an instance of the choropleth for a given year
    choroplethkey = year + '~' + agency + '~' + locality + '~ALL'
    
    # options to draw bar chart for all localities, single agency
    bar1key = year + '~' + agency + '~ALL~' + industry
    
    # options to draw bar chart for single locality, all agencies
    bar2key = year + '~ALL~' + locality + '~' + industry
    
    # options to draw bar chart for all localities, all agencies
    bar3key = year + '~ALL~ALL~' + industry
    
    # options to draw line chart for all localities, all agencies
    line1key = year + '~ALL~ALL~ALL'
    
    # options to draw line chart for all localities, single agency
    line2key = year + '~' + agency + '~ALL~ALL'
    
    # options to draw line chart for single locality, single agency
    #line3key = year + '~' + agency + '~' + locality + '~ALL'
    
    # options to draw line chart for single locality, all agencies, all industries
    line4key = year + '~ALL~' + locality + '~ALL'
    
    alldata = addfunding(alldata, choroplethkey, funding)
    alldata = addfunding(alldata, bar1key, funding)
    alldata = addfunding(alldata, bar2key, funding)
    alldata = addfunding(alldata, bar3key, funding)
    alldata = addfunding(alldata, line1key, funding)
    alldata = addfunding(alldata, line2key, funding)
    #alldata = addfunding(alldata, line3key, funding)
    alldata = addfunding(alldata, line4key, funding)

    return alldata

def main(args):

    inputfilename = args[1]
    outputfilename = args[2]

    years = []
    agencies = []
    cities = []
    industries = []

    alldata = {}

    with open(inputfilename, 'rU') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')

        for row in csvreader:

            year = row['year']
            agency = row['agency']
            locality = row['locality']
            funding = D(row['funding'])
            industry = row['industry']

            alldata = generateCombinations(alldata, year, agency, locality, funding, industry)

    output = open(outputfilename, 'w')

    csvwriter = csv.writer(output, delimiter='\t', quotechar='"')

    csvwriter.writerow( [ 'year', 'agency', 'locality', 'industry', 'funding' ] )

    for key in alldata.keys():
        keys = key.split('~')
        keys.extend(list((alldata[key], )))
        csvwriter.writerow( keys )

    output.close()

if __name__ == '__main__':
    main(sys.argv)
