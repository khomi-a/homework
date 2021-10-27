import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--name", required=True)
parser.add_argument("--country", required=True)
parser.add_argument("--petal-colour", required=True, choices=["R", "W", "Y", "V", "B"])
parser.add_argument("--stem-length", required=True, type=int)
parser.add_argument("--with-thorns", action='store_true')
parser.add_argument("--companion-plants", default=None, nargs='*')

with open('journal.txt', 'a') as out:
    arguments = vars(parser.parse_args())
    json.dump(arguments, out)
