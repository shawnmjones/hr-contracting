#!/usr/bin/env python

import sys
import csv

def main(args):

    filenames = args[1:-1]
    outputfile = args[-1]

    print "starting processing..."
    print "given {} files to process".format(len(filenames))
    print "using {} as output file, OVERWRITING IT IF IT EXISTS!!!".format(outputfile)

    output = open(outputfile, 'w')
    csvwriter = csv.writer(output, delimiter=',', quotechar='"')

    for filename in filenames:
        print "processing {} for data".format(filename)

        # convert to CSV
        # extract data from following columns:
        #   * subaward_major_agency_name (CD) - 82
        #   * subaward_amount (BU) - 73
        #   * subaward_principle_place_city (BN) - 66
        #   * subaward_principle_naics_desc (BX) - 76
        #   * subaward_fiscal_year (CK) - 89
        with open(filename, 'rb') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in csvreader:
                csvwriter.writerow( [ row[88], row[81], row[65], row[72], row [75] ] )

    output.close()
         

if __name__ == '__main__':
    main(sys.argv)
