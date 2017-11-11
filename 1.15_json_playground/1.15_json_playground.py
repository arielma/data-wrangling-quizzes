# This Python file uses the following encoding: utf-8
#import os, sys

"""
To experiment with this code freely you will have to run this code locally.
Take a look at the main() function for an example of how to use the code. We
have provided example json output in the other code editor tabs for you to look
at, but you will not be able to run any queries through our UI.
"""
import json
import requests
import pprint

BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"


# query parameters are given to the requests.get function as a dictionary; this
# variable contains some starter parameters.
query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


def has_tag_name_kurt(artist):
    return 'tags' in artist and any(tag['name'] == "kurt cobain" for tag in artist['tags'])


def query_site(url, params, uid="", fmt="json"):
    """
    This is the main function for making queries to the musicbrainz API. The
    query should return a json document.
    """
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print "requesting", r.url

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    """
    This adds an artist name to the query parameters before making an API call
    to the function above.
    """
    params["query"] = "artist:" + name
    return query_site(url, params)


def pretty_print(data, indent=4):
    """
    After we get our output, we can use this function to format it to be more
    readable.
    """
    if type(data) == dict:
        print json.dumps(data, indent=indent, sort_keys=True,ensure_ascii=False).encode('utf8')
    else:
        print data


def main():
    """
    Below is an example investigation to help you get started in your
    exploration. Modify the function calls and indexing below to answer the
    questions on the next quiz.

    HINT: Note how the output we get from the site is a multi-level JSON
    document, so try making print statements to step through the structure one
    level at a time or copy the output to a separate output file. Experimenting
    and iteration will be key to understand the structure of the data!
    """

    # Query for information in the database about bands named FIRST AND KIT
    results = query_by_name(ARTIST_URL, query_type["simple"], "FIRST AND KIT")
    print 'How many bands named FIRST AND KIT?'
    print len(results['artists'])  # or print result['count']

    # Query for information in the database about QUEEN
    results_queen = query_by_name(ARTIST_URL, query_type["simple"], 'QUEEN')
    print 'Begin-area name for QUEEN:'
    for artist in results_queen['artists']:
        if artist['name'] == 'Queen' and 'begin-area' in artist:
            print artist['begin-area']['name']
            break

    # Query for information in the database for Beatles
    results_beatles = query_by_name(ARTIST_URL, query_type["simple"], 'BEATLES')
    # pretty_print(results_beatles)
    print 'Spanish alias for BEATLES:'

    artists_beatles = [artist for artist in results_beatles['artists'] if artist['name'] == 'The Beatles']
    # note artists_beatles will be a list
    alias_es = [alias for alias in artists_beatles[0]['aliases'] if alias['locale'] == 'es']
    print alias_es[0]['name']

    '''
    Alternatively using for loop:
    # for artist in results_beatles['artists']:
    #     if artist['name'] == 'The Beatles':
    #         for alias in artist['aliases']:
    #             if alias['locale'] == 'es':
    #                 print alias['name']
    #                 break;
    '''

    # Query for information in the database about Nirvana
    print 'Disambiguation for Nirvana which Kurt Cobain is in:'
    results_nirvana = query_by_name(ARTIST_URL, query_type["simple"], 'NIRVANA')
    # using filter to first find all artists whose name exactly is Nirvana
    artists_nirvana = list(filter(lambda artist: artist['name'] == 'Nirvana', results_nirvana['artists']))

    # Using filter to find out artist who has a tag named kurt cobain
    artist_nirvana_kurt = list(filter(has_tag_name_kurt, artists_nirvana))
    nirvana_disambiguations = [a['disambiguation'] for a in artist_nirvana_kurt ]
    for d in nirvana_disambiguations:
        print d

    # Query for information in the database about One Direction
    print 'Disambiguation for Nirvana which Kurt Cobain is in:'
    results_one_direction = query_by_name(ARTIST_URL, query_type["simple"], 'One Direction')
    results_one_direction_exact = list(filter(lambda artist: artist['name'] == 'One Direction', results_one_direction['artists']))
    one_direction_start_year = [a['life-span']['begin'] for a in results_one_direction_exact]
    for y in one_direction_start_year:
        print y


if __name__ == '__main__':
    main()