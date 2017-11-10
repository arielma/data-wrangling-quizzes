#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format

"""
import os
import xlrd
import pprint
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data"
datafile_unzipped = '2013_ERCOT_Hourly_Load_Data.xls'

# unzip the zip file
def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()

# parse the xls file
def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    print "Number of rows in the sheet:",
    print sheet.nrows
    # get values in the COAST column without the header
    col_coast = sheet.col_values(1, start_rowx=1, end_rowx=None)

    # Find the maximum value
    col_coast_max = max(col_coast)
    # Find the row number of the maximum value. Plus 1 to add the header
    col_coast_max_pos = col_coast.index(max(col_coast)) + 1
    # find and return the time value for the max entry
    col_coast_max_time = xlrd.xldate_as_tuple(sheet.cell_value(col_coast_max_pos, 0), 0)

    col_coast_min = min(col_coast)
    col_coast_min_pos = col_coast.index(min(col_coast)) + 1
    col_coast_min_time = xlrd.xldate_as_tuple(sheet.cell_value(col_coast_min_pos, 0), 0)


    print "Max value in Coast Region is:"
    print col_coast_max
    print "At row index:"
    print col_coast_max_pos
    print "Time for the max value is:"
    print col_coast_max_time

    print "\nMin value in Coast Region is:"
    print col_coast_min
    print "At row index:"
    print col_coast_min_pos
    print "Time for the min value is:"
    print col_coast_min_time

    print "\nAverage value in Coast Region is:"
    print sum(col_coast)/len(col_coast)



    data = {
            'maxtime': col_coast_max_time,
            'maxvalue': col_coast_max,
            'mintime': col_coast_min_time,
            'minvalue': col_coast_min,
            'avgcoast': sum(col_coast)/len(col_coast)
    }
    pprint.pprint(data)
    return data


def test():
    open_zip(datafile)
    data = parse_file(datafile_unzipped)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)

if __name__ == '__main__':
    test()