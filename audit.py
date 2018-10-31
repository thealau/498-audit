import csv
import sys
import argparse
import openElectionsParser

def parse_args(argv):
    policy_file = ''
    data_file = ''
    parser = argparse.ArgumentParser(description = "Description for my parser")
    parser.add_argument("-H", "--Help", help = "Example: Help argument", required = False, default = "")
    parser.add_argument("-s", "--save", help = "Example: Save argument", required = False, default = "")
    parser.add_argument("-p", "--print", help = "Example: Print argument", required = False, default = "")
    parser.add_argument("-o", "--output", help = "Example: Output argument", required = False, default = "")

    argument = parser.parse_args()
    status = False

    if argument.Help:
        print("You have used '-H' or '--Help' with argument: {0}".format(argument.Help))
        status = True
    if argument.save:
        print("You have used '-s' or '--save' with argument: {0}".format(argument.save))
        status = True
    if argument.print:
        print("You have used '-p' or '--print' with argument: {0}".format(argument.print))
        status = True
    if argument.output:
        print("You have used '-o' or '--output' with argument: {0}".format(argument.output))
        status = True
    if not status:
        print("Maybe you want to use -H or -s or -p or -p as arguments ?") 

def precinct_count(audited, precincts):
    n = 4794
    total = 1
    for x in range(0, 299):
        total *= (n - x) / (n - x + 6)
    print(total)

if __name__ == "__main__":
   openElectionsParser.parse("20161108__mi__general__precinct.csv", 'precinct', 'President')
