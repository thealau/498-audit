import csv
import sys
import argparse
import openElectionsParser
from math import ceil

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

def audit_precinct(percentage, data_dict):
    state_wide_sorted = sorted(data_dict["vote_totals"].items(), key=lambda kv: kv[1], reverse=True)
    difference = state_wide_sorted[0][1] - state_wide_sorted[1][1]
    votes_to_flip = difference/2
    winner_name = state_wide_sorted[0][0]
    second_place = state_wide_sorted[1][0]
    total_num_precincts = len(data_dict["results"])
    precincts_sorted = sorted(data_dict["results"], key=lambda k: k["vote_totals"][winner_name], reverse=True)
    winner_total = 0
    count = 0
    while winner_total < votes_to_flip:
        winner_total += precincts_sorted[count]["vote_totals"][winner_name]
        count += 1
    num_to_flip = count
    prob_miss_interf = 1
    for i in range(0, ceil(percentage*total_num_precincts)):
        prob_miss_interf *= (total_num_precincts - i - num_to_flip)/(total_num_precincts - i)
    print("Probability of detecting interference:", round(1 - prob_miss_interf, 2))



if __name__ == "__main__":
   data_dict = openElectionsParser.parse("20161108__wi__general__ward.csv", 'ward', 'President')
   audit_precinct(.05, data_dict)
