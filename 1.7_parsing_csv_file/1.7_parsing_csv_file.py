# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os
import csv
import pprint


DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_csv(datafile):
    data = []
    n = 0
    with open(datafile, "rb") as sd:
        r = csv.DictReader(sd)
        for line in r:
            data.append(line)

    return data


if __name__ == '__main__':
    datafile = os.path.join(DATADIR, DATAFILE)
    # parse_csv(datafile)
    d = parse_csv(datafile)
    pprint.pprint(d)