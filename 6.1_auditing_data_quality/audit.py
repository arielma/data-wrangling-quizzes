#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up. In the first exercise we want you to audit
the datatypes that can be found in some particular fields in the dataset.
The possible types of values can be:
- NoneType if the value is a string "NULL" or an empty string ""
- list, if the value starts with "{"
- int, if the value can be cast to int
- float, if the value can be cast to float, but CANNOT be cast to int.
   For example, '3.23e+07' should be considered a float because it can be cast
   as float but int('3.23e+07') will throw a ValueError
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and a
SET of the types that can be found in the field. e.g.
{"field1": set([type(float()), type(int()), type(str())]),
 "field2": set([type(str())]),
  ....
}
The type() function returns a type object describing the argument given to the
function. You can also use examples of objects to create type objects, e.g.
type(1.1) for a float: see the test function below for examples.

Note that the first three rows (after the header row) in the cities.csv file
are not actual data points. The contents of these rows should note be included
when processing data types. Be sure to include functionality in your code to
skip over or detect these rows.
"""
import codecs
import csv
import json
import pprint


CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label",
          "isPartOf_label", "areaCode", "populationTotal", "elevation",
          "maximumElevation", "minimumElevation", "populationDensity",
          "wgs84_pos#lat", "wgs84_pos#long", "areaLand", "areaMetro", "areaUrban"]

def is_int_try(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def is_float_try(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def audit_file(filename, fields):
    cities = []
    fieldtypes = {}
    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        for count, city in enumerate(reader):
            if count >= 3:
                cities.append(city)

        for field in fields:
            field_type_set = set()
            for city in cities:
                if (city[field] == "NULL" or city[field] == ""):
                    field_type_set.add(type(None))
                elif city[field].startswith('{'):
                    field_type_set.add(type([]))
                elif is_int_try(city[field]):
                    field_type_set.add(type(1))
                elif is_float_try(city[field]):
                    field_type_set.add(type(1.1))
                else:
                    field_type_set.add(type(str()))
            fieldtypes[field] = field_type_set

    return fieldtypes


def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])

if __name__ == "__main__":
    test()
